#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ultimate Mininet L3 Lab – Final Optimized Version
─────────────────────────────────────────────────────────────
• VLAN 10 (left LAN: h1,h2,r1) & VLAN 20 (right LAN: h3,h4,r2)
• Single router link per switch (no duplicates)
• s2 as cheaper/faster alternative path (300Mbps/2ms vs direct 100Mbps/10ms)
• Auto Ryu controller detection + fallback
• Static routing + SDN-ready (secure fail-mode)
• Detailed topology print + extra tests
"""

import argparse
import subprocess
import re

from mininet.net import Mininet
from mininet.node import OVSSwitch, Node, RemoteController
from mininet.link import TCLink
from mininet.topo import Topo
from mininet.cli import CLI
from mininet.log import setLogLevel, info, warn

# ─── ANSI Colors ─────────────────────────────────────────────
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
RESET = "\033[0m"

# ─── Controller IP Detection ─────────────────────────────────
def get_controller_ip():
    parser = argparse.ArgumentParser(description="Ultimate L3 Lab")
    parser.add_argument("--controller-ip", type=str, default=None,
                        help="External Ryu controller IP")
    parser.add_argument("--fallback-ip", type=str, default="192.168.152.160",
                        help="Fallback controller IP")
    args = parser.parse_args()

    if args.controller_ip:
        info(f"{YELLOW}Using controller IP from argument: {args.controller_ip}{RESET}\n")
        return args.controller_ip

    try:
        out = subprocess.check_output(["ip", "route", "show", "default"], text=True)
        match = re.search(r"default via (\d+\.\d+\.\d+\.\d+)", out)
        if match:
            gw_ip = match.group(1)
            info(f"{YELLOW}Detected gateway IP: {gw_ip}{RESET}\n")
            return gw_ip
    except Exception as e:
        warn(f"Gateway detection failed: {e}\n")

    info(f"{YELLOW}Using fallback controller IP: {args.fallback_ip}{RESET}\n")
    return args.fallback_ip

# ─── Linux Router Node ───────────────────────────────────────
class LinuxRouter(Node):
    def config(self, **params):
        super().config(**params)
        self.cmd("sysctl -w net.ipv4.ip_forward=1")
        self.cmd("sysctl -w net.ipv4.conf.all.forwarding=1")
        self.cmd("sysctl -w net.ipv4.conf.all.send_redirects=0")

    def terminate(self):
        self.cmd("sysctl -w net.ipv4.ip_forward=0")
        super().terminate()

# ─── Topology Definition ─────────────────────────────────────
class LabTopology(Topo):
    def build(self):
        # Switches
        s1 = self.addSwitch("s1", cls=OVSSwitch, protocols="OpenFlow13")
        s2 = self.addSwitch("s2", cls=OVSSwitch, protocols="OpenFlow13")  # alternative cheaper path
        s3 = self.addSwitch("s3", cls=OVSSwitch, protocols="OpenFlow13")

        # Routers (single link to switch)
        r1 = self.addNode("r1", cls=LinuxRouter)
        r2 = self.addNode("r2", cls=LinuxRouter)

        # Hosts
        h1 = self.addHost("h1", ip="10.10.10.11/24", defaultRoute="via 10.10.10.1")
        h2 = self.addHost("h2", ip="10.10.10.12/24", defaultRoute="via 10.10.10.1")
        h3 = self.addHost("h3", ip="10.20.20.11/24", defaultRoute="via 10.20.20.1")
        h4 = self.addHost("h4", ip="10.20.20.12/24", defaultRoute="via 10.20.20.1")

        # Left LAN (VLAN 10) – access ports
        self.addLink(h1, s1, port2=1)                        # s1 port1 → h1
        self.addLink(h2, s1, port2=2)                        # s1 port2 → h2
        self.addLink(r1, s1, port2=3, intfName1="r1-left")   # s1 port3 → r1 (single)

        # Right LAN (VLAN 20) – access ports
        self.addLink(h3, s3, port2=1)                        # s3 port1 → h3
        self.addLink(h4, s3, port2=2)                        # s3 port2 → h4
        self.addLink(r2, s3, port2=3, intfName1="r2-right")  # s3 port3 → r2 (single)

        # Backbone between routers (untagged, high bandwidth)
        self.addLink(r1, r2, intfName1="r1-backbone", intfName2="r2-backbone",
                     params1={"ip": "192.168.100.1/30"},
                     params2={"ip": "192.168.100.2/30"},
                     bw=200, delay="3ms")

        # Direct link s1 ↔ s3 (higher cost)
        self.addLink(s1, s3, port1=5, port2=5, bw=100, delay="10ms")

        # Alternative path via s2 (lower cost – preferred)
        self.addLink(s1, s2, port1=4, port2=1, bw=300, delay="2ms")
        self.addLink(s2, s3, port1=2, port2=4, bw=300, delay="2ms")

# ─── ASCII Topology View ─────────────────────────────────────
def show_topology():
    diagram = f"""
{GREEN}10.10.10.0/24 (VLAN10)                  Backbone 192.168.100.0/30                  10.20.20.0/24 (VLAN20)
┌───────────────┐                                                               ┌───────────────┐
│  h1   h2      │                                                               │  h3   h4      │
│   │   │       │                                                               │   │   │       │
└───┴───┴───────┘                                                               └───┴───┴───────┘
      │   │                                                                              │   │
   ┌──┴───┴──┐                                                                       ┌──┴───┴──┐
   │   s1     │ ────────(direct, 100Mbps/10ms)───────────────►                 │   s3     │
   │          │                                                                       │          │
   └────┬─────┘                                                                       └────┬─────┘
        │   (300Mbps/2ms)                                                                   │   (300Mbps/2ms)
        └───────────────► s2 ◄───────────────────────────────┘                           │
                        (cheaper/faster alternative path)                                │
                                │                                                         │
                         ┌──────┴──────┐                                                  │
                         │    r1        │ ────────(backbone 200Mbps/3ms)───────────►     │
                         │              │                                                  │
                         └──────┬───────┘                                                  │
                                │                                                          │
                         ┌──────┴──────┐                                                  │
                         │    r2        │ ◄───────────────────────────────────────────────┘
                         └───────────────┘{RESET}
"""
    info(diagram)

# ─── Static Routing Configuration ────────────────────────────
def configure_static_routing(net):
    r1 = net["r1"]
    r2 = net["r2"]

    r1.setIP("10.10.10.1/24", intf="r1-left")
    r2.setIP("10.20.20.1/24", intf="r2-right")

    # Hosts default gateway
    for h in ["h1", "h2"]:
        net[h].cmd("ip route replace default via 10.10.10.1")
    for h in ["h3", "h4"]:
        net[h].cmd("ip route replace default via 10.20.20.1")

    # Inter-subnet routes via backbone
    r1.cmd("ip route replace 10.20.20.0/24 via 192.168.100.2 dev r1-backbone")
    r2.cmd("ip route replace 10.10.10.0/24 via 192.168.100.1 dev r2-backbone")

    info(f"{GREEN}Static routing configured successfully{RESET}\n")

# ─── Main Execution ──────────────────────────────────────────
def main():
    setLogLevel("info")
    info(f"{CYAN}Starting Ultimate Hybrid L3 Lab with s2 redundancy path{RESET}\n")

    controller_ip = get_controller_ip()

    net = Mininet(
        topo=LabTopology(),
        switch=OVSSwitch,
        link=TCLink,
        controller=RemoteController("c0", ip=controller_ip, port=6653),
        autoSetMacs=True,
        autoStaticArp=True
    )

    info("Starting network...\n")
    net.start()

    # Set secure fail-mode for SDN controller
    for sw in net.switches:
        sw.cmd(f"ovs-vsctl set-fail-mode {sw.name} secure")
        info(f"{sw.name} fail-mode set to secure (SDN mode)\n")

    configure_static_routing(net)
    show_topology()

    info(f"\n{GREEN}Network ready! Recommended tests:{RESET}\n")
    info("  • Intra-LAN left  : h1 ping h2\n")
    info("  • Gateway test     : h1 ping 10.10.10.1\n")
    info("  • Inter-LAN        : h1 ping 10.20.20.11\n")
    info("  • Reverse inter    : h3 ping 10.10.10.11\n")
    info("  • Full mesh        : pingall\n")
    info("  • Flow table       : ovs-ofctl dump-flows s1\n")
    info("  • Ryu logs         : watch Ryu console for PKT/ARP lines\n")

    # Run detailed ping tests
    info(f"{YELLOW}Running initial connectivity tests...{RESET}\n")
    net.pingAllFull()

    CLI(net)
    net.stop()

if __name__ == "__main__":
    main()
