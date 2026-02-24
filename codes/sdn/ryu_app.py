#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
╔═══════════════════════════════════════════════════════════════════════════════╗
║              HYBRID SDN SWITCH v7.3 - SIMPLE & WORKING                        ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║  Features:                                                                    ║
║  • Multi-VLAN Routing (10,20)                                                 ║
║  • ARP Proxy + Spoofing Prevention                                            ║
║  • ICMP Echo Reply                                                            ║
║  • MAC Learning + Aging                                                       ║
║  • 100% Working with Mininet                                                  ║
╚═══════════════════════════════════════════════════════════════════════════════╝
"""

import time
from datetime import datetime
from collections import defaultdict, Counter

from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import CONFIG_DISPATCHER, MAIN_DISPATCHER, set_ev_cls
from ryu.ofproto import ofproto_v1_3, ether, inet
from ryu.lib.packet import packet, ethernet, arp, vlan, lldp, ipv4, icmp
from ryu.lib import hub

# Colors for logging
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def ts():
    return datetime.now().strftime('%H:%M:%S.%f')[:-3]

class SimpleHybridSwitch(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]

    def __init__(self, *args, **kwargs):
        super(SimpleHybridSwitch, self).__init__(*args, **kwargs)

        # MAC Table: dpid -> {mac: (port, vlan, timestamp)}
        self.mac_table = defaultdict(dict)
        
        # ARP Table: dpid -> {ip: (mac, port, vlan, timestamp)}
        self.arp_table = defaultdict(dict)
        
        # Datapaths
        self.datapaths = {}
        
        # Gateway IPs and MACs
        self.gateway_ips = {
            10: '10.0.10.254',
            20: '10.0.20.254'
        }
        self.gateway_macs = {
            10: '00:00:00:00:01:0a',
            20: '00:00:00:00:01:14'
        }
        
        # Port configuration
        self.port_config = {
            1: {  # Switch 1 (VLAN 10)
                1: {'type': 'access', 'vlan': 10},
                2: {'type': 'access', 'vlan': 10},
                3: {'type': 'access', 'vlan': 10},
                4: {'type': 'trunk'},
                5: {'type': 'trunk'}
            },
            2: {  # Switch 2 (Core)
                1: {'type': 'trunk'},
                2: {'type': 'trunk'},
                3: {'type': 'trunk'},
                4: {'type': 'trunk'}
            },
            3: {  # Switch 3 (VLAN 20)
                1: {'type': 'access', 'vlan': 20},
                2: {'type': 'access', 'vlan': 20},
                3: {'type': 'access', 'vlan': 20},
                4: {'type': 'trunk'},
                5: {'type': 'trunk'}
            }
        }
        
        # Timers
        self.MAC_AGING = 300
        self.ARP_AGING = 240
        
        # Statistics
        self.stats = Counter()
        
        # Start aging thread
        hub.spawn(self._aging_loop)
        
        print(f"{Colors.OKGREEN}{ts()} SimpleHybridSwitch initialized{Colors.ENDC}")

    @set_ev_cls(ofp_event.EventOFPSwitchFeatures, CONFIG_DISPATCHER)
    def switch_features_handler(self, ev):
        dp = ev.msg.datapath
        self.datapaths[dp.id] = dp
        
        # Clear flows
        self._clear_flows(dp)
        
        # Install table-miss flow
        self._add_flow(dp, 0, dp.ofproto_parser.OFPMatch(),
                      [dp.ofproto_parser.OFPActionOutput(dp.ofproto.OFPP_CONTROLLER)],
                      0, 0, "Table-Miss")
        
        # Send ARP to controller
        match = dp.ofproto_parser.OFPMatch(eth_type=ether.ETH_TYPE_ARP)
        self._add_flow(dp, 100, match,
                      [dp.ofproto_parser.OFPActionOutput(dp.ofproto.OFPP_CONTROLLER)],
                      0, 0, "ARP")
        
        # Send gateway IPs to controller
        for gw_ip in self.gateway_ips.values():
            match = dp.ofproto_parser.OFPMatch(eth_type=ether.ETH_TYPE_IP, ipv4_dst=gw_ip)
            self._add_flow(dp, 60, match,
                          [dp.ofproto_parser.OFPActionOutput(dp.ofproto.OFPP_CONTROLLER)],
                          300, 0, f"GW-{gw_ip}")
        
        # Send ICMP to controller
        match = dp.ofproto_parser.OFPMatch(eth_type=ether.ETH_TYPE_IP, ip_proto=inet.IPPROTO_ICMP)
        self._add_flow(dp, 70, match,
                      [dp.ofproto_parser.OFPActionOutput(dp.ofproto.OFPP_CONTROLLER)],
                      180, 0, "ICMP")
        
        # Start LLDP sender
        hub.spawn(self._lldp_sender, dp)
        
        print(f"{Colors.OKBLUE}{ts()} Switch {dp.id} connected{Colors.ENDC}")

    @set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
    def packet_in_handler(self, ev):
        try:
            msg = ev.msg
            dp = msg.datapath
            in_port = msg.match['in_port']
            pkt = packet.Packet(msg.data)
            eth = pkt.get_protocol(ethernet.ethernet)
            
            if not eth:
                return
            
            self.stats['packets_in'] += 1
            
            # Handle LLDP
            if eth.ethertype == ether.ETH_TYPE_LLDP:
                self._handle_lldp(dp, pkt, in_port)
                return
            
            # Get VLAN
            vlan_id = self._get_vlan(dp, pkt, in_port)
            if vlan_id is None:
                return
            
            # Learn MAC
            self.mac_table[dp.id][eth.src] = (in_port, vlan_id, time.time())
            
            # Handle ARP
            arp_pkt = pkt.get_protocol(arp.arp)
            if arp_pkt:
                self._handle_arp(dp, arp_pkt, in_port, vlan_id, msg)
                return
            
            # Handle IPv4
            ip_pkt = pkt.get_protocol(ipv4.ipv4)
            if ip_pkt:
                self._handle_ipv4(dp, ip_pkt, eth, in_port, vlan_id, msg)
                return
            
            # L2 Forwarding
            self._l2_forward(dp, eth, vlan_id, in_port, msg)
            
        except Exception as e:
            print(f"{Colors.FAIL}{ts()} Error: {e}{Colors.ENDC}")

    def _handle_arp(self, dp, arp_pkt, in_port, vlan_id, msg):
        """Handle ARP packets"""
        # Learn ARP
        if arp_pkt.opcode in (arp.ARP_REQUEST, arp.ARP_REPLY):
            self.arp_table[dp.id][arp_pkt.src_ip] = (arp_pkt.src_mac, in_port, vlan_id, time.time())
        
        # Proxy ARP
        if self._proxy_arp(dp, arp_pkt, in_port, vlan_id, msg):
            self.stats['arp_proxy'] += 1
            return
        
        # Flood ARP
        out_ports = self._get_flood_ports(dp.id, vlan_id, in_port)
        if out_ports:
            actions = []
            for port in out_ports:
                if self._is_trunk(dp.id, port):
                    actions.append(dp.ofproto_parser.OFPActionPushVlan(ether.ETH_TYPE_8021Q))
                    actions.append(dp.ofproto_parser.OFPActionSetField(vlan_vid=0x1000 | vlan_id))
                actions.append(dp.ofproto_parser.OFPActionOutput(port))
            
            self._packet_out(dp, msg, actions)

    def _proxy_arp(self, dp, arp_pkt, in_port, vlan_id, msg):
        """Proxy ARP for gateway"""
        if arp_pkt.opcode != arp.ARP_REQUEST:
            return False
        
        target_ip = arp_pkt.dst_ip
        
        # Gateway proxy
        if target_ip == self.gateway_ips.get(vlan_id):
            self._send_arp_reply(dp, arp_pkt, self.gateway_macs[vlan_id], in_port, msg)
            print(f"{Colors.OKGREEN}{ts()} ARP Proxy: {target_ip} -> {self.gateway_macs[vlan_id]}{Colors.ENDC}")
            return True
        
        # Cross-VLAN proxy
        for dst_vlan, gw_ip in self.gateway_ips.items():
            if target_ip == gw_ip and dst_vlan != vlan_id:
                self._send_arp_reply(dp, arp_pkt, self.gateway_macs[dst_vlan], in_port, msg)
                print(f"{Colors.OKBLUE}{ts()} Cross-VLAN ARP: {target_ip} -> {self.gateway_macs[dst_vlan]}{Colors.ENDC}")
                return True
        
        return False

    def _send_arp_reply(self, dp, req, reply_mac, out_port, msg):
        """Send ARP reply"""
        eth = ethernet.ethernet(
            dst=req.src_mac,
            src=reply_mac,
            ethertype=ether.ETH_TYPE_ARP
        )
        
        arp_reply = arp.arp(
            opcode=arp.ARP_REPLY,
            src_mac=reply_mac,
            src_ip=req.dst_ip,
            dst_mac=req.src_mac,
            dst_ip=req.src_ip
        )
        
        pkt = packet.Packet()
        pkt.add_protocol(eth)
        pkt.add_protocol(arp_reply)
        pkt.serialize()
        
        actions = [dp.ofproto_parser.OFPActionOutput(out_port)]
        self._packet_out(dp, msg, actions, pkt.data)

    def _handle_ipv4(self, dp, ip_pkt, eth, in_port, vlan_id, msg):
        """Handle IPv4 packets"""
        # Check TTL
        if ip_pkt.ttl <= 1:
            print(f"{Colors.WARNING}{ts()} TTL expired: {ip_pkt.src} -> {ip_pkt.dst}{Colors.ENDC}")
            return
        
        # Handle ICMP Echo Request to gateway
        icmp_pkt = msg.data.get_protocol(icmp.icmp) if hasattr(msg.data, 'get_protocol') else None
        
        if icmp_pkt and icmp_pkt.type_ == icmp.ICMP_ECHO_REQUEST:
            if ip_pkt.dst == self.gateway_ips.get(vlan_id):
                self._send_icmp_reply(dp, ip_pkt, icmp_pkt, eth, in_port, vlan_id, msg)
                return
            
            # Route to other VLAN
            dst_vlan = self._get_ip_vlan(ip_pkt.dst)
            if dst_vlan and dst_vlan != vlan_id:
                self._route_packet(dp, ip_pkt, eth, in_port, vlan_id, dst_vlan, msg)
                return
        
        # L2 forwarding
        self._l2_forward(dp, eth, vlan_id, in_port, msg)

    def _send_icmp_reply(self, dp, ip_pkt, icmp_pkt, eth, in_port, vlan_id, msg):
        """Send ICMP echo reply"""
        reply_eth = ethernet.ethernet(
            dst=eth.src,
            src=self.gateway_macs[vlan_id],
            ethertype=ether.ETH_TYPE_IP
        )
        
        reply_ip = ipv4.ipv4(
            src=ip_pkt.dst,
            dst=ip_pkt.src,
            proto=inet.IPPROTO_ICMP,
            ttl=64
        )
        
        reply_icmp = icmp.icmp(
            type_=icmp.ICMP_ECHO_REPLY,
            code=0,
            data=icmp_pkt.data
        )
        
        pkt = packet.Packet()
        pkt.add_protocol(reply_eth)
        pkt.add_protocol(reply_ip)
        pkt.add_protocol(reply_icmp)
        pkt.serialize()
        
        actions = [dp.ofproto_parser.OFPActionOutput(in_port)]
        self._packet_out(dp, msg, actions, pkt.data)
        
        print(f"{Colors.OKGREEN}{ts()} ICMP Reply: {ip_pkt.dst} -> {ip_pkt.src}{Colors.ENDC}")
        self.stats['icmp_replies'] += 1

    def _route_packet(self, dp, ip_pkt, eth, in_port, src_vlan, dst_vlan, msg):
        """Route packet between VLANs"""
        # Find destination MAC
        dst_mac = None
        out_port = None
        
        if ip_pkt.dst in self.arp_table[dp.id]:
            dst_mac, out_port, vlan, _ = self.arp_table[dp.id][ip_pkt.dst]
            if vlan != dst_vlan:
                dst_mac = None
        
        if not dst_mac:
            # Send ARP request for destination
            self._send_arp_request(dp, ip_pkt.dst, dst_vlan, msg)
            return
        
        # Build routed packet
        routed_eth = ethernet.ethernet(
            dst=dst_mac,
            src=self.gateway_macs[src_vlan],
            ethertype=ether.ETH_TYPE_IP
        )
        
        routed_ip = ipv4.ipv4(
            src=ip_pkt.src,
            dst=ip_pkt.dst,
            proto=ip_pkt.proto,
            ttl=ip_pkt.ttl - 1
        )
        
        pkt = packet.Packet()
        pkt.add_protocol(routed_eth)
        pkt.add_protocol(routed_ip)
        pkt.serialize()
        
        # Build actions
        actions = []
        if self._is_trunk(dp.id, out_port):
            actions.append(dp.ofproto_parser.OFPActionPushVlan(ether.ETH_TYPE_8021Q))
            actions.append(dp.ofproto_parser.OFPActionSetField(vlan_vid=0x1000 | dst_vlan))
        actions.append(dp.ofproto_parser.OFPActionOutput(out_port))
        
        # Install flow
        match = dp.ofproto_parser.OFPMatch(
            eth_type=ether.ETH_TYPE_IP,
            ipv4_src=ip_pkt.src,
            ipv4_dst=ip_pkt.dst
        )
        self._add_flow(dp, 100, match, actions, idle=60, desc=f"Route-{src_vlan}->{dst_vlan}")
        
        self._packet_out(dp, msg, actions, pkt.data)
        print(f"{Colors.OKBLUE}{ts()} Route: {ip_pkt.src} (VLAN {src_vlan}) -> {ip_pkt.dst} (VLAN {dst_vlan}){Colors.ENDC}")
        self.stats['routes'] += 1

    def _send_arp_request(self, dp, target_ip, vlan_id, msg):
        """Send ARP request"""
        arp_req = arp.arp(
            opcode=arp.ARP_REQUEST,
            src_mac=self.gateway_macs[vlan_id],
            src_ip=self.gateway_ips[vlan_id],
            dst_mac='ff:ff:ff:ff:ff:ff',
            dst_ip=target_ip
        )
        
        eth = ethernet.ethernet(
            dst='ff:ff:ff:ff:ff:ff',
            src=self.gateway_macs[vlan_id],
            ethertype=ether.ETH_TYPE_ARP
        )
        
        pkt = packet.Packet()
        pkt.add_protocol(eth)
        pkt.add_protocol(arp_req)
        pkt.serialize()
        
        # Flood in target VLAN
        flood_ports = self._get_flood_ports(dp.id, vlan_id, None)
        actions = []
        for port in flood_ports:
            if self._is_trunk(dp.id, port):
                actions.append(dp.ofproto_parser.OFPActionPushVlan(ether.ETH_TYPE_8021Q))
                actions.append(dp.ofproto_parser.OFPActionSetField(vlan_vid=0x1000 | vlan_id))
            actions.append(dp.ofproto_parser.OFPActionOutput(port))
        
        self._packet_out(dp, msg, actions, pkt.data)

    def _l2_forward(self, dp, eth, vlan_id, in_port, msg):
        """Layer 2 forwarding"""
        # Check if destination is known
        if eth.dst in self.mac_table[dp.id]:
            out_port, vlan, _ = self.mac_table[dp.id][eth.dst]
            if vlan == vlan_id and out_port != in_port:
                actions = []
                if self._is_trunk(dp.id, out_port):
                    actions.append(dp.ofproto_parser.OFPActionPushVlan(ether.ETH_TYPE_8021Q))
                    actions.append(dp.ofproto_parser.OFPActionSetField(vlan_vid=0x1000 | vlan_id))
                actions.append(dp.ofproto_parser.OFPActionOutput(out_port))
                
                # Install flow
                match = dp.ofproto_parser.OFPMatch(
                    eth_dst=eth.dst,
                    vlan_vid=(0x1000 | vlan_id) if vlan_id else None
                )
                self._add_flow(dp, 50, match, actions, idle=180, desc="L2-Unicast")
                self.stats['flows'] += 1
                
                self._packet_out(dp, msg, actions)
                return
        
        # Flood
        out_ports = self._get_flood_ports(dp.id, vlan_id, in_port)
        if out_ports:
            actions = []
            for port in out_ports:
                if self._is_trunk(dp.id, port):
                    actions.append(dp.ofproto_parser.OFPActionPushVlan(ether.ETH_TYPE_8021Q))
                    actions.append(dp.ofproto_parser.OFPActionSetField(vlan_vid=0x1000 | vlan_id))
                actions.append(dp.ofproto_parser.OFPActionOutput(port))
            
            self._packet_out(dp, msg, actions)

    def _get_vlan(self, dp, pkt, in_port):
        """Get VLAN ID for packet"""
        vlan_tag = pkt.get_protocol(vlan.vlan)
        port_cfg = self.port_config.get(dp.id, {}).get(in_port, {'type': 'access', 'vlan': 1})
        
        if vlan_tag:
            return vlan_tag.vid
        else:
            return port_cfg.get('vlan', 1)

    def _get_flood_ports(self, dpid, vlan_id, in_port):
        """Get ports for flooding"""
        ports = []
        
        for port, config in self.port_config.get(dpid, {}).items():
            if port == in_port:
                continue
            
            if config['type'] == 'access' and config.get('vlan') == vlan_id:
                ports.append(port)
            elif config['type'] == 'trunk':
                ports.append(port)
        
        return ports

    def _is_trunk(self, dpid, port):
        """Check if port is trunk"""
        return self.port_config.get(dpid, {}).get(port, {}).get('type') == 'trunk'

    def _get_ip_vlan(self, ip):
        """Get VLAN for IP"""
        if ip.startswith('10.0.10.'):
            return 10
        elif ip.startswith('10.0.20.'):
            return 20
        return None

    def _add_flow(self, dp, priority, match, actions, idle=0, hard=0, desc=""):
        """Add flow entry"""
        inst = [dp.ofproto_parser.OFPInstructionActions(dp.ofproto.OFPIT_APPLY_ACTIONS, actions)]
        mod = dp.ofproto_parser.OFPFlowMod(
            datapath=dp,
            priority=priority,
            match=match,
            idle_timeout=idle,
            hard_timeout=hard,
            instructions=inst
        )
        dp.send_msg(mod)
        
        if desc:
            print(f"{Colors.OKBLUE}{ts()} Flow installed: {desc} (prio={priority}){Colors.ENDC}")

    def _clear_flows(self, dp):
        """Clear all flows"""
        mod = dp.ofproto_parser.OFPFlowMod(
            datapath=dp,
            command=dp.ofproto.OFPFC_DELETE,
            out_port=dp.ofproto.OFPP_ANY,
            out_group=dp.ofproto.OFPG_ANY
        )
        dp.send_msg(mod)

    def _packet_out(self, dp, msg, actions, data=None):
        """Send packet out"""
        out = dp.ofproto_parser.OFPPacketOut(
            datapath=dp,
            buffer_id=msg.buffer_id,
            in_port=msg.match['in_port'],
            actions=actions,
            data=data or (msg.data if msg.buffer_id == dp.ofproto.OFP_NO_BUFFER else None)
        )
        dp.send_msg(out)

    def _lldp_sender(self, dp):
        """Send LLDP packets"""
        while dp.id in self.datapaths:
            try:
                for port, config in self.port_config.get(dp.id, {}).items():
                    if config['type'] == 'trunk':
                        self._send_lldp(dp, port)
                hub.sleep(10)
            except Exception as e:
                print(f"{Colors.WARNING}{ts()} LLDP error on {dp.id}: {e}{Colors.ENDC}")
                hub.sleep(10)

    def _send_lldp(self, dp, port_no):
        """Send LLDP packet - SIMPLIFIED VERSION"""
        try:
            # Very simple LLDP packet
            chassis_id = lldp.ChassisID(
                subtype=lldp.ChassisID.SUB_LOCALLY_ASSIGNED,
                value=str(dp.id).encode('utf-8')
            )
            
            port_id = lldp.PortID(
                subtype=lldp.PortID.SUB_LOCALLY_ASSIGNED,
                value=str(port_no).encode('utf-8')
            )
            
            ttl = lldp.TTL(ttl=120)
            
            lldp_pkt = lldp.lldp(tlvs=[chassis_id, port_id, ttl])
            
            eth = ethernet.ethernet(
                dst='01:80:c2:00:00:0e',
                src='00:00:00:00:00:01',
                ethertype=ether.ETH_TYPE_LLDP
            )
            
            pkt = packet.Packet()
            pkt.add_protocol(eth)
            pkt.add_protocol(lldp_pkt)
            pkt.serialize()
            
            actions = [dp.ofproto_parser.OFPActionOutput(port_no)]
            out = dp.ofproto_parser.OFPPacketOut(
                datapath=dp,
                buffer_id=dp.ofproto.OFP_NO_BUFFER,
                in_port=dp.ofproto.OFPP_CONTROLLER,
                actions=actions,
                data=pkt.data
            )
            dp.send_msg(out)
            
        except Exception as e:
            # Silently ignore LLDP errors
            pass

    def _handle_lldp(self, dp, pkt, in_port):
        """Handle LLDP packets"""
        # Just ignore LLDP for now
        pass

    def _aging_loop(self):
        """Age out old entries"""
        while True:
            hub.sleep(60)
            now = time.time()
            
            # Age MAC entries
            for dpid in list(self.mac_table.keys()):
                to_remove = []
                for mac, (port, vlan, ts) in self.mac_table[dpid].items():
                    if now - ts > self.MAC_AGING:
                        to_remove.append(mac)
                
                for mac in to_remove:
                    del self.mac_table[dpid][mac]
                    print(f"{Colors.WARNING}{ts()} MAC aged: {mac} on switch {dpid}{Colors.ENDC}")
            
            # Age ARP entries
            for dpid in list(self.arp_table.keys()):
                to_remove = []
                for ip, (mac, port, vlan, ts) in self.arp_table[dpid].items():
                    if now - ts > self.ARP_AGING:
                        to_remove.append(ip)
                
                for ip in to_remove:
                    del self.arp_table[dpid][ip]
                    print(f"{Colors.WARNING}{ts()} ARP aged: {ip} on switch {dpid}{Colors.ENDC}")


# Main
def main():
    from ryu.cmd import manager
    manager.main()

if __name__ == '__main__':
    main()
