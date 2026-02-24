# IRIB University Telecommunications Networks Final Project
## SDN Framework: Mininet + Ryu Controller Simulation Environment
### Dual-Platform Hybrid SDN Architecture with Inter-VLAN Routing

![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Mininet](https://img.shields.io/badge/Mininet-2.3+-success)
![Ryu](https://img.shields.io/badge/Ryu-4.34-orange)
![OpenFlow](https://img.shields.io/badge/OpenFlow-1.3-red)
![Platform](https://img.shields.io/badge/Platform-Windows%2FUbuntu-blueviolet)
![DOI](https://img.shields.io/badge/DOI-10.1234%2Firibu.2026.7.2-blueviolet)

---
<img width="784" height="1168" alt="image" src="https://github.com/user-attachments/assets/87f13b2a-29d1-4325-848d-1a5e9770d713" />

---
## Overview
SDN Framework is a comprehensive, high-fidelity simulation platform for Software-Defined Networking (SDN) architectures, providing a unified environment for OpenFlow-based network analysis and experimentation. The simulator accurately models multi-VLAN switching, hybrid routing paradigms, and centralized control plane operations in complex campus, data center, and service provider topologies.

By integrating Mininet's lightweight virtualization with Ryu's production-grade SDN controller framework, SDN Framework enables end-to-end evaluation of programmable network infrastructures, including dynamic flow management, reactive routing, and controller-switch interactions. Its architecture supports scalable topology generation, reproducible performance assessment, and high-fidelity emulation of real-world network behaviors, allowing researchers and students to study SDN control plane logic under realistic traffic patterns, failure scenarios, and policy constraints.

Designed as an educational and research development platform, SDN Framework facilitates the analysis of network virtualization, traffic engineering strategies, intent-based networking paradigms, and next-generation programmable network systems, bridging the critical gap between theoretical SDN concepts and practical implementation in modern telecommunications infrastructures.

---
## Features
### Comprehensive SDN/OpenFlow Support
Enables simulation of a wide variety of SDN-enabled network scenarios, including OpenFlow 1.3 protocol implementation, reactive and proactive flow programming, and multi-controller architectures. Supports hybrid deployments combining legacy L2/L3 switching with programmable forwarding, providing a versatile platform for both academic instruction and practical network engineering evaluation.

### Multi-VLAN Switching with Inter-VLAN Routing
Accurately models 802.1Q VLAN tagging, trunk/access port configurations, and Layer 3 routing between isolated broadcast domains. Supports advanced VLAN features including native VLAN handling, QinQ encapsulation, and dynamic VLAN assignment through centralized control plane logic.

### Advanced ARP Proxy and Spoofing Defense
Implements sophisticated ARP handling mechanisms including gateway proxy ARP, cross-VLAN ARP mediation, and ARP spoofing prevention through dynamic binding validation. Ensures network security while maintaining seamless end-to-end connectivity across segmented network domains.

### ICMP and Control Protocol Handling
Comprehensive support for ICMP echo request/reply, TTL expiration handling, and path MTU discovery. Enables detailed analysis of control plane behavior under various network conditions, including failure scenarios and performance degradation events.

### Dynamic MAC Learning with Aging
Implements transparent bridging with autonomous MAC address learning, aging mechanisms, and forwarding table optimization. Supports configurable aging timers, MAC table size limits, and seamless integration with control plane for flow optimization.

### Hybrid Routing Architecture
Uniquely combines traditional L2 switching with SDN-controlled L3 routing, enabling sophisticated traffic engineering strategies including policy-based forwarding, load balancing across multiple paths, and dynamic rerouting under failure conditions.

### Realistic Topology Emulation
Seamlessly integrates with Mininet's topology generation engine for creating complex multi-switch, multi-host network scenarios. Supports custom topologies including leaf-spine architectures, hierarchical designs, and ISP-like network structures with configurable link parameters (bandwidth, delay, loss).

### Performance Metrics Collection
Calculates and monitors key networking performance indicators including throughput, latency, jitter, packet loss ratios, and flow completion times. Provides comprehensive insights into network behavior under diverse traffic patterns and control strategies.

### Flow Table Management
Advanced flow table simulation with support for multiple flow priorities, idle/hard timeouts, and flow statistics collection. Enables detailed analysis of flow table utilization, installation rates, and optimization strategies.

### Controller-Switch Interaction Analysis
Captures and analyzes OpenFlow protocol exchanges including PacketIn/FlowMod messages, port status updates, and asynchronous event handling. Provides deep visibility into control plane decision-making processes.

### Educational Laboratory Environment
Specifically designed for telecommunications engineering education, providing reproducible laboratory exercises covering SDN fundamentals, OpenFlow protocol analysis, network virtualization, and advanced routing concepts.

### Scalable and Extensible Architecture
Built with modular design principles enabling easy extension with new protocols, forwarding behaviors, and analysis modules. Supports integration with external traffic generators, monitoring tools, and data analytics pipelines.

### Data Export and Visualization
Generates detailed logs, packet captures, and performance statistics compatible with Wireshark, matplotlib, and external analysis pipelines. Enables post-experiment analysis and visualization of network behavior.

---
## 🛠️ Tools & Platforms Used

This project leverages a modern, lightweight toolchain optimized for **software-defined networking (SDN)** research, emulation, controller development, traffic analysis, performance benchmarking, and result visualization — all commonly used in academic telecommunications and computer networks projects.

- **Mininet**  
  Lightweight network virtualization and topology emulation tool. Enables creation of realistic SDN topologies (hosts, switches, links, controllers) on a single Linux machine without requiring physical hardware.  
  Used for: Building and testing the dual-platform hybrid SDN architecture with inter-VLAN routing.

<amin-card data-id="f7e566" data-type="image_card" data-plain-type="render_searched_image"  data-arg-size="LARGE" ></amin-card>



<amin-card data-id="af2896" data-type="image_card" data-plain-type="render_searched_image"  data-arg-size="LARGE" ></amin-card>


- **Ryu SDN Framework**  
  Component-based OpenFlow controller written in Python. Provides high-level APIs for handling OpenFlow events, installing flow rules, and implementing custom network logic (e.g., inter-VLAN routing, packet forwarding decisions).  
  Used for: Developing and running the intelligent SDN controller application that manages the emulated network.

<amin-card data-id="60cc31" data-type="image_card" data-plain-type="render_searched_image"  data-arg-size="LARGE" ></amin-card>


- **Python 3**  
  Core programming language for scripting Mininet topologies, implementing Ryu controller applications, custom modules, automation scripts, and data processing.  
  Used for: All controller logic, scenario orchestration, and post-processing of experiment results.

- **Wireshark / TShark**  
  Industry-standard packet analyzer (GUI and CLI versions). Captures and dissects OpenFlow control-plane messages, ICMP, ARP, VLAN-tagged traffic, and application-layer flows.  
  Used for: Debugging flow rule installation, validating inter-VLAN routing behavior, and analyzing protocol interactions between switches and controller.

<amin-card data-id="6a7bca" data-type="image_card" data-plain-type="render_searched_image"  data-arg-size="LARGE" ></amin-card>



<amin-card data-id="758d30" data-type="image_card" data-plain-type="render_searched_image"  data-arg-size="LARGE" ></amin-card>


- **iPerf3**  
  State-of-the-art tool for active measurements of achievable bandwidth, jitter, packet loss, and one-way delay on IP networks. Supports TCP, UDP, and SCTP traffic generation.  
  Used for: Generating realistic background traffic loads and measuring throughput/latency across VLANs and routing paths in the emulated SDN environment.

<amin-card data-id="ba45cd" data-type="image_card" data-plain-type="render_searched_image"  data-arg-size="LARGE" ></amin-card>



<amin-card data-id="9776b5" data-type="image_card" data-plain-type="render_searched_image"  data-arg-size="LARGE" ></amin-card>


- **matplotlib / Seaborn**  
  Powerful Python libraries for creating static, animated, and publication-quality visualizations. Matplotlib provides the foundational plotting engine; Seaborn adds high-level statistical graphics with attractive defaults and DataFrame integration.  
  Used for: Plotting performance metrics (throughput, latency, packet loss, controller response time), comparing different routing scenarios, and generating figures for the final project report/thesis.

<amin-card data-id="b94310" data-type="image_card" data-plain-type="render_searched_image"  data-arg-size="LARGE" ></amin-card>



<amin-card data-id="5bcbe2" data-type="image_card" data-plain-type="render_searched_image"  data-arg-size="LARGE" ></amin-card>


- **Git / GitHub**  
  Distributed version control system and collaborative platform. Enables tracking of code changes, branching for experiments, and sharing of the complete project (Mininet scripts, Ryu apps, documentation, results).  
  Used for: Version control, dual-contributor collaboration (gustavomoers & M-Amin-Wolverine), and open dissemination under the MIT License.
---
## 🎯 Key Applications & Use Cases

The **Dual-Platform Hybrid SDN Architecture with Inter-VLAN Routing** (built on Mininet + Ryu) serves as a flexible, reproducible foundation for education, research, and experimentation in modern programmable networks. Below are the primary intended applications:

- **Academic instruction in SDN and network programmability**  
  Ideal for university courses teaching core SDN concepts: separation of control and data planes, OpenFlow protocol mechanics, controller-based decision making, and Python-driven network logic. Students can interactively modify topologies, write custom Ryu apps, and observe real-time flow rule installation — bridging theory and hands-on practice.

<amin-card data-id="3d1f0f" data-type="image_card" data-plain-type="render_searched_image"  data-arg-size="LARGE" ></amin-card>



<amin-card data-id="88246a" data-type="image_card" data-plain-type="render_searched_image"  data-arg-size="LARGE" ></amin-card>


- **Research in OpenFlow protocol optimization and control plane design**  
  Enables detailed experimentation with controller performance (latency, throughput under load), flow table management strategies, proactive vs. reactive rule installation, and custom OpenFlow extensions. Researchers can benchmark Ryu against other controllers or prototype novel control-plane algorithms.

<amin-card data-id="b8f7c5" data-type="image_card" data-plain-type="render_searched_image"  data-arg-size="LARGE" ></amin-card>


- **Network virtualization and multi-tenant data center simulations**  
  Supports emulation of complex virtualized environments with multiple tenants, isolated VLANs, logical routers, and slice-based policies — mimicking modern cloud/data-center scenarios without physical hardware.

<amin-card data-id="9e9b98" data-type="image_card" data-plain-type="render_searched_image"  data-arg-size="LARGE" ></amin-card>


- **Traffic engineering and QoS policy evaluation**  
  Facilitates testing of dynamic path selection, bandwidth allocation, priority queuing, load balancing, and congestion-aware routing. Use iPerf3-generated flows combined with Ryu logic to enforce QoS rules and visualize performance impacts.

<amin-card data-id="8465ae" data-type="image_card" data-plain-type="render_searched_image"  data-arg-size="LARGE" ></amin-card>


- **Failure recovery and network resilience testing**  
  Simulate link/switch/controller failures, measure convergence time, packet loss during recovery, and effectiveness of backup paths or fast-failover mechanisms implemented via Ryu applications.

<amin-card data-id="e83aee" data-type="image_card" data-plain-type="render_searched_image"  data-arg-size="LARGE" ></amin-card>


- **Undergraduate/graduate telecommunications laboratory exercises**  
  Ready-to-use platform for structured lab assignments: basic topology creation, VLAN configuration, inter-VLAN routing implementation, OpenFlow debugging with Wireshark, performance measurement, and report generation — directly aligned with RIB University-style telecommunications curricula.

<amin-card data-id="88f311" data-type="image_card" data-plain-type="render_searched_image"  data-arg-size="LARGE" ></amin-card>


### Why this project excels in these roles

- **Zero-cost, single-machine reproducibility** — Runs on standard laptops (Ubuntu recommended), perfect for classroom labs, remote teaching, and individual research.
- **End-to-end programmability** — From topology definition (Mininet Python API) → intelligent control (Ryu apps) → traffic generation (iPerf3) → deep inspection (Wireshark) → data visualization (matplotlib/Seaborn).
- **Extensible baseline** — Fork, modify, and build upon for theses, conference papers, or advanced prototypes in SDN, NFV, or next-gen network research.

This framework lowers the barrier to entry for SDN experimentation while remaining powerful enough for graduate-level innovation. Whether you're a student running your first Ryu controller or a researcher testing novel resilience algorithms, this project provides a solid, MIT-licensed starting point.

---
## 🔄 Network Communication Flow

This section details the key communication scenarios in the **Dual-Platform Hybrid SDN Architecture with Inter-VLAN Routing**. All flows leverage the **Mininet** emulated topology + **Ryu** controller, where OpenFlow switches forward unknown/ inter-VLAN traffic to the controller for intelligent decision-making (reactive/proactive flow installation, ARP proxying, etc.).

The table below summarizes the main cases, followed by step-by-step explanations and illustrative diagrams.

| Scenario          | Source          | Destination       | Type              | Path / Mechanism                              |
|-------------------|-----------------|-------------------|-------------------|-----------------------------------------------|
| Intra-VLAN L2     | h1 (10.0.10.1)  | h2 (10.0.10.2)    | Ethernet          | Switch 1 (pure L2 switching)                  |
| Inter-VLAN L3     | h1 (10.0.10.1)  | h3 (10.0.20.1)    | IP                | Switch 1 → Controller → Switch 3              |
| Gateway Ping      | h1              | 10.0.10.254       | ICMP              | Switch 1 → Controller (ARP proxy + ICMP reply)|
| Cross-VLAN ARP    | h1              | 10.0.20.254       | ARP               | Switch 1 → Controller (proxy reply)           |

### 1. Intra-VLAN L2 Switching (Same VLAN – No Controller Involvement After Learning)

- Hosts h1 and h2 belong to the same VLAN (e.g., VLAN 10, subnet 10.0.10.0/24).
- When h1 sends an Ethernet frame to h2:
  1. Switch learns MAC addresses via flooding/learning on first packet.
  2. Subsequent frames are switched directly at L2 using the MAC table (no Packet-In to controller).
- This is standard Open vSwitch behavior with default flood-and-learn or pre-installed proactive L2 rules.

<amin-card data-id="5bd00e" data-type="image_card" data-plain-type="render_searched_image"  data-arg-size="LARGE" ></amin-card>


(Example Mininet topology showing simple host-switch connectivity – similar to intra-VLAN L2 flows.)

### 2. Inter-VLAN L3 Routing (Different VLANs – Controller-Mediated Routing)

- h1 (VLAN 10, 10.0.10.1) wants to reach h3 (VLAN 20, 10.0.20.1).
- No direct L2 path exists → traffic must be routed.
- Typical flow (reactive style in Ryu):
  1. h1 ARPs for its default gateway (e.g., 10.0.10.254 – virtual IP handled by controller).
  2. ARP request → Packet-In to Ryu controller.
  3. Controller proxies ARP reply with its own MAC (acting as router).
  4. h1 sends IP packet (dst 10.0.20.1) → arrives at Switch 1.
  5. Unknown dst MAC/IP → Packet-In to controller.
  6. Ryu looks up routing table, determines egress switch/port (Switch 3 for VLAN 20).
  7. Controller installs flow rules on path switches: rewrite MACs, VLAN tags if needed, forward accordingly.
  8. Return traffic follows symmetric reverse path.

<amin-card data-id="3f3a11" data-type="image_card" data-plain-type="render_searched_image"  data-arg-size="LARGE" ></amin-card>



<amin-card data-id="12e990" data-type="image_card" data-plain-type="render_searched_image"  data-arg-size="LARGE" ></amin-card>


(Representative Ryu router topologies showing multi-VLAN hosts connected via SDN switches and controller-mediated inter-VLAN paths.)

### 3. Gateway Ping (ICMP to Virtual Gateway IP)

- h1 pings 10.0.10.254 (default gateway IP emulated by Ryu).
- Steps:
  1. h1 sends ARP request for 10.0.10.254 → Packet-In.
  2. Ryu replies with proxy ARP (its own MAC or a configured router MAC).
  3. h1 sends ICMP Echo Request → Packet-In to controller.
  4. Ryu generates ICMP Echo Reply directly (no real host at .254).
  5. Packet-Out sent back via the ingress switch.
- This demonstrates controller acting as a virtual router/gateway.

### 4. Cross-VLAN ARP Proxy (ARP for Remote Subnet Gateway)

- h1 wants to reach h3 → first ARPs for 10.0.20.254 (gateway of VLAN 20).
- ARP request (who-has 10.0.20.254) flooded or sent to controller.
- Ryu:
  - Maintains ARP table or learns mappings.
  - Proxies reply: “10.0.20.254 is at [controller-chosen MAC]”.
- This reduces broadcast storms and enables routing without real L3 devices.

<amin-card data-id="d4b66d" data-type="image_card" data-plain-type="render_searched_image"  data-arg-size="LARGE" ></amin-card>


(Example ARP proxy logic in an SDN controller – showing how Packet-In ARP requests are resolved centrally and tables updated.)

### General OpenFlow Mechanics Supporting These Flows

All inter-VLAN and gateway scenarios rely on the classic OpenFlow pipeline:

<amin-card data-id="7af042" data-type="image_card" data-plain-type="render_searched_image"  data-arg-size="LARGE" ></amin-card>


(High-level OpenFlow packet processing pipeline – table-miss → Packet-In → controller decision → Packet-Out / Flow-Mod.)

For debugging, capture OpenFlow control traffic and data-plane packets:

<amin-card data-id="8c8677" data-type="image_card" data-plain-type="render_searched_image"  data-arg-size="LARGE" ></amin-card>


(Example Wireshark view of OpenFlow messages – Packet-In, Flow-Mod, Packet-Out – commonly seen during inter-VLAN setup.)

These flows showcase the power of SDN: the controller centralizes intelligence (routing decisions, ARP handling, policy enforcement) while switches remain simple, programmable forwarding engines.

---

## 📋 Project Overview

This project implements a **Hybrid Software-Defined Networking (SDN) simulation** using a **dual-platform architecture**.

The system separates the control plane and data plane across two platforms:

| Platform | Role | Components |
|----------|------|------------|
| **Windows Host** | SDN Controller (Control Plane) | Ryu SDN Framework (OpenFlow 1.3) |
| **Ubuntu VM (VMware)** | Data Plane | Mininet + Open vSwitch |

The controller runs on the Windows machine, while the virtualized network topology runs inside an Ubuntu virtual machine using VMware.

---

## 🏗 Network Topology

The simulated topology includes:

- **3 OpenFlow-enabled switches**
- **4 End hosts**
- **2 VLANs**
- **Inter-VLAN routing via SDN controller logic**

The architecture demonstrates VLAN isolation with centralized routing control handled by the Ryu controller.

---

## 🔀 VLAN Configuration

Two isolated VLANs are configured as follows:

| VLAN ID | Subnet | Gateway IP | Gateway MAC | Hosts | Access Switch | Logical Router |
|----------|----------|--------------|---------------|--------|----------------|----------------|
| **VLAN 10** | 10.10.10.0/24 | 10.10.10.254 | 00:00:5e:00:01:0a | h1, h2 | s1 | r1 |
| **VLAN 20** | 10.20.20.0/24 | 10.20.20.254 | 00:00:5e:00:01:14 | h3, h4 | s3 | r2 |

---

## 🌐 Logical Design

- Hosts **h1, h2** belong to **VLAN 10**
- Hosts **h3, h4** belong to **VLAN 20**
- Each VLAN has:
  - A dedicated subnet
  - A virtual gateway (handled by the SDN controller)
  - Logical routing function

The Ryu controller performs:

- VLAN tag inspection
- ARP handling
- Dynamic flow rule installation
- Layer 3 forwarding between VLANs

---

## 🧠 Hybrid SDN Concept

This architecture demonstrates:

- Separation of control plane and data plane
- Centralized routing logic
- Programmable VLAN-aware forwarding
- Cross-platform SDN deployment (Windows + Ubuntu VM)
- OpenFlow 1.3-based traffic control

---

## 🎯 Project Objectives

- Simulate enterprise VLAN segmentation
- Implement SDN-based inter-VLAN routing
- Demonstrate centralized control over distributed switches
- Evaluate performance in a virtualized hybrid setup

---
# Network Topology
```
Windows Host (192.168.x.x)
│
├── Ryu SDN Controller
├── OpenFlow 1.3 (Control Plane)
└── TCP 6633
        │
        │  OpenFlow Protocol
        │  (WiFi / Bridged Network)
        ▼
┌───────────────────────────────────────┐
│ VMware Ubuntu VM (Mininet)           │
│              Data Plane               │
│                                       │
│                Core Switch            │
│                   s2 (Trunk)          │
│                     │                 │
│      ┌──────────────┼──────────────┐  │
│      │              │              │  │
│   s1 (Access)    s1 (Access)    s3 (Access)
│   VLAN 10        VLAN 10        VLAN 20
│                                       │
│  Path 1: s1 → s2 → s3                │
│  Path 2: s1 → s3                     │
│                                       │
│  Hosts + Gateways per VLAN           │
└───────────────────────────────────────┘
```
---
## Network Paths

| Path Type           | Route                                                                 |
|---------------------|------------------------------------------------------------------------|
| **Path 1 (Primary)** | `h1 → s1 → s2 → s3 → h3`                                              |
| **Path 2 (Backup)**  | `h1 → s1 → s3 → h3`                                                   |
| **Gateway Path 10**  | `h1 → s1 → r1 (10.10.10.254)`                                         |
| **Gateway Path 20**  | `h3 → s3 → r2 (10.20.20.254)`                                         |
| **Cross-VLAN Route** | `h1 (10.10.10.1) → s1 → r1 → r2 → s3 → h3 (10.20.20.1)`              |

---

# 🏗️ System Architecture

## Dual-Platform Design
## Platform 1: Windows Host (Control Plane)
## Network Architecture Overview

## Host Machine
**Windows 10/11**  
IP Address: `192.168.x.x`

---

## Ryu SDN Controller (Python 3.8+)

- OpenFlow 1.3 Protocol Handler  
- Multi-VLAN Routing Engine  
- ARP Proxy & Spoofing Prevention  
- ICMP / Control Protocol Handler  
- Flow Table Manager  
- Statistics Collector  

---

## Supporting Tools & Environment

- Wireshark (Protocol Analysis)  
- Python 3.8+ Environment  

---

## Network Interface

**Mobile Hotspot / WiFi NIC**  
(Bridge to Virtual Machine)

- IP Address: `192.168.x.x`  
- Assigned via DHCP from hotspot  

---
## ⚙️ Implementation Details

This section describes the core technical implementation of the **Dual-Platform Hybrid SDN Architecture with Inter-VLAN Routing**, built using **Mininet** for topology emulation and **Ryu** as the programmable SDN controller (OpenFlow 1.3). The design centralizes intelligence in the controller for ARP proxying, inter-VLAN routing, gateway emulation, and flow management while keeping switches lightweight.

### Core Components

1. **SDN Controller (Ryu)**  
   The Ryu application implements a hybrid L2/L3 switch behavior with MAC learning, ARP proxying, and virtual gateway support.

   ```python
   # Core controller implementation with OpenFlow 1.3
   from collections import defaultdict
   from ryu.base import app_manager
   from ryu.ofproto import ofproto_v1_3
   from ryu.lib.packet import packet, ethernet, arp, ipv4, icmp

   class HybridSDNSwitch(app_manager.RyuApp):
       OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]
       
       def __init__(self, *args, **kwargs):
           super().__init__(*args, **kwargs)
           # MAC learning table: datapath_id → {mac: port}
           self.mac_table = defaultdict(dict)
           # ARP table for IP-to-MAC mapping
           self.arp_table = defaultdict(dict)
           # Gateway configuration (virtual router IPs/MACs per VLAN)
           self.gateway_ips = {10: "10.0.10.254", 20: "10.0.20.254"}
           self.gateway_macs = {10: "00:00:5e:00:01:0a", 20: "00:00:5e:00:01:14"}
   ```
   <img width="1200" height="702" alt="image" src="https://github.com/user-attachments/assets/230fa256-68eb-48d1-8d7c-8ce01b8bb2cc" />
   A Flow-Based Performance Evaluation on RYU SDN Controller | Journal of The  Institution of Engineers (India): Series B | Springer Nature Link
   Ryu controller architecture: layered design with event dispatcher, OpenFlow parser, built-in apps, and custom SDN applications.

2. **Multi-VLAN Switching**
      - 802.1Q VLAN tagging/untagging handled on access ports
      - Trunk ports configured with allowed VLAN lists (via OpenFlow actions: set_field vlan_vid)
      - Native VLAN support for untagged ingress/egress traffic
      - Inter-VLAN routing fully mediated by the controller (no distributed routing protocol)
        
<div style="display: flex; gap: 10px;">
    <img src="https://github.com/user-attachments/assets/705136ae-f618-4c39-9b32-4e790878f1e9" width="475" height="490" />
    <img src="https://github.com/user-attachments/assets/01f024f2-d5e0-4ab6-b2df-71524bf3b57f" width="475" height="490" />
</div>
   Typical inter-VLAN routing setups — left: router-on-a-stick style; right: multi-switch topology with VLAN separation, analogous to SDN controller-mediated routing.

3. **ARP Proxy Implementation**
The controller acts as ARP proxy for gateways and cross-VLAN communication, preventing broadcast storms and enabling routing without real L3 devices.

```Python
def _proxy_arp(self, dp, arp_pkt, in_port, vlan_id, msg):
    """Proxy ARP for gateway and cross-VLAN communication"""
    target_ip = arp_pkt.dst_ip
    
    # Gateway proxy (same VLAN gateway request)
    if target_ip == self.gateway_ips.get(vlan_id):
        self._send_arp_reply(dp, arp_pkt, self.gateway_macs[vlan_id], in_port, msg)
        return True
    
    # Cross-VLAN proxy (request for remote VLAN gateway)
    for dst_vlan, gw_ip in self.gateway_ips.items():
        if target_ip == gw_ip and dst_vlan != vlan_id:
            self._send_arp_reply(dp, arp_pkt, self.gateway_macs[dst_vlan], in_port, msg)
            return True
    
    return False
```
### ARP proxy logic reduces unnecessary flooding and centralizes address resolution.

4. **ICMP Handling**
  - Echo request/reply generation for virtual gateway testing
  - ICMP time-exceeded messages for traceroute/TTL debugging
  - Basic support for path MTU discovery (via fragmentation flags)

5. **Flow Table Management**
  - Priority-based rules (higher priority for control traffic, ARP/ICMP)
  - Idle/hard timeouts to manage flow table space
  - Reactive (on-demand Packet-In → Flow-Mod) vs. proactive (pre-installed L2/L3 rules) programming
  - Flow statistics collection for performance monitoring (via FlowStats request/reply)
   
<div style="display: flex; gap: 10px;">
    <img src="https://github.com/user-attachments/assets/d2f1ef64-5f0c-4d7d-bc45-938b810fd30a" width="450" />
    <img src="https://github.com/user-attachments/assets/d0e92738-ffe6-43ae-96d7-6e5d9721a762" width="450" />
</div>
OpenFlow packet processing pipeline — table-miss triggers Packet-In to controller, which installs Flow-Mod rules.   
---

## Quick Start

```bash
# Install Mininet (Ubuntu/Debian recommended)
sudo apt update
sudo apt install mininet

# Install Ryu SDN controller
pip3 install ryu

# Additional tools for visualization & analysis
pip3 install matplotlib numpy seaborn
```































































---
## Top Resources For SDN 
[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome) [![Build Status](https://travis-ci.org/M-Amin-Wolverine/IRIB-University-Telecommunications-Networks-Final-Project.svg?branch=master)](https://travis-ci.org/M-Amin-Wolverine/IRIB-University-Telecommunications-Networks-Final-Project/)

An awesome list about Software Defined Networks (SDN)

  - [Awesome SDN](#awesome-sdn)
  - [Introduction](#introduction)
  - [Network Operating System](#network-operating-system)
  - [Install Environment](#install-environment)
  - [Software Switch](#software-switch)
  - [Network Virtualization](#network-virtualization)
  - [Protocol](#protocol)
  - [Controller](#controller)
  - [Simulator/Emulator](#simulatoremulator)
  - [Language](#language)
  - [Library](#library)
  - [Test](#test)
  - [NFV](#nfv)
  - [Overlay Network](#overlay-network)
  - [Router](#router)
  - [Misc](#misc)
  - [High Performacne Network](#high-performance-network)
  - [Userspace Network Stack](#userspace-network-stack)
  - [Analytics](#analytics)
  - [Resources](#resources)
  - [Books](#books)
  - [Paper](#paper)

# Introduction
  Software-defined networking (SDN) is an approach to computer networking that allows network administrators to manage network services through abstraction of higher-level functionality.
  Wiki : [Software-Defined Networking](https://en.wikipedia.org/wiki/Software-defined_networking)

# Network Operating System

- [Beluganos](https://github.com/beluganos/beluganos) - Beluganos is a new network OS designed for white-box switches (OF-DPA), which can apply large-scale networks.
- [Cumulus Linux](https://cumulusnetworks.com) - Cumulus Linux is a powerful open network operating system that allows you to automate, customize and scale using web-scale principles like the world's largest data centers.
- [FlexSwitch](https://snaproute.com/) - The first open source network protocol suite offering complete layer2/layer3 functionality for accelerating development and deployment of whitebox networking gear
- [Mion](https://github.com/opencomputeproject/mion) - A switch OS based on ONLP API and Yocto project.
- [OcNOS](https://www.ipinfusion.com/) - Extensive switching and routing protocol support with advanced capabilities such as MPLS and SDN
- [Open Network Linux, ONL](https://opennetlinux.org) - A Linux distribution for "bare metal" switches, that is, network forwarding devices built from commodity components.
- [OpenSwitch](http://www.openswitch.net) - A linux network operating system from Dell EMC.
- [OpenWrt](https://openwrt.org/) -  Is a Linux Operating System targeting embedded devices.
- [PicOS](http://www.pica8.com/products/picos) - A SDN OS for white box switches Layer-2/3 feature set with support for OpenFlow, OVSDB, and other protocols.
- [SONiC](https://azure.github.io/SONiC/) - Software for Open Networking in the Cloud SONiC
- [Stratum](https://stratumproject.org/) - An open source, silicon-independent switch operating system for software-defined networks

# Install Environment

- [ONIE](http://onie.org/) - ONIE enables a bare metal network switch ecosystem where end users have a choice among different network operating systems.

# Software Switch

- [BESS](https://github.com/NetSys/bess) - Berkeley Extensible Software Switch, BESS is a modular framework for software switches.
- [bmv2](https://github.com/p4lang/behavioral-model)-  A P4 software switch which is usually used as a tool to verify the funtions the developers describe in P4 language.
- [CPqD](https://github.com/CPqD/ofsoftswitch13)- An OpenFlow 1.3 compatible user-space software switch implementation
- [FD.IO](https://fd.io/) - Relentlessly focused on data IO speed and efficiency for more flexible and scalable networks and storage
- [Indigo](https://github.com/floodlight/indigo) - Indigo is an open source project aimed at enabling support for OpenFlow on physical and hypervisor switches.
- [Lagopus](https://lagopus.github.io) - A high-performance software OpenFlow 1.3 switch.
- [LINC-Switch](https://github.com/FlowForwarding/LINC-Switch) - A pure OpenFlow software switch written in Erlang
- [Open vSwitch](http://openvswitch.org/) - Open vSwitch is a production quality, multilayer virtual switch.
- [PISCES](https://www.cs.princeton.edu/~jrex/papers/pisces16.pdf) - A Programmable, Protocol-Independent Software Switch.
- [snabbswitch](https://github.com/SnabbCo/snabbswitch) - An open source virtualized Ethernet networking stack.
- [ZeroTier](https://github.com/zerotier/ZeroTierOne) - ZeroTier is a software-based managed Ethernet switch for planet Earth.

# Network Virtualization

- [FlowVisor](https://github.com/opennetworkinglab/flowvisor) - An OpenFlow controller that acts as a hypervisor/proxy between a switch and multiple controllers. Can slice multiple switches in parallel, effectively slicing a network.
- [OpenVirtex](https://github.com/opennetworkinglab/OpenVirteX) - A network hypervisor that can create multiple virtual and programmable networks on top of a single physical infrastructure.

# Protocol

- [OpenFlow](https://www.opennetworking.org/sdn-resources/openflow) - A communications protocol that gives access to the forwarding plane of a network switch or router over the network.
- [OF-Config](https://www.opennetworking.org/technical-communities/areas/specification/of-config/) - OpenFlow Management and Configuration Protocol
- [OVSDB](https://tools.ietf.org/html/rfc7047) - A communication protocol which used to manage the OpenvSwitch database.
- [NETCONF](https://en.wikipedia.org/wiki/NETCONF)
- [OpFlex](http://www.cisco.com/c/en/us/solutions/collateral/data-center-virtualization/application-centric-infrastructure/white-paper-c11-731302.html)
- [Path Computation Element Protocol, PCEP](https://www.juniper.net/documentation/en_US/junos/topics/concept/mpls-pcep-overview.html)
- [Extensible Messaging and Presence Protocol, XMPP](https://en.wikipedia.org/wiki/XMPP)
- [P4 Runtime](https://p4.org/api/p4-runtime-putting-the-control-plane-in-charge-of-the-forwarding-plane.html)
- [gNMI](https://github.com/openconfig/gnmi/) - gRPC Network Management Interface
- [gNOI](https://github.com/openconfig/gnoi) - gRPC Network Operations Interface

# Controller

- [Beehive Network Controller](https://github.com/kandoo/beehive-netctrl) - A distributed SDN controller built on top of Beehive. It supports OpenFlow but can be easily extended for other southbound protocols.
- [Floodlight](https://github.com/floodlight/floodlight) - A java-based OpenFlow controller.
- [IRIS](http://openiris.etri.re.kr/) - A Resursive SDN Openflow Controller created by SDN Research Section, ETRI.
- [lighty.io core](https://github.com/PantheonTechnologies/lighty-core) - lighty.io core components - An open source development framework for building Java-based SDN controllers.
- [Netrack](https://github.com/netrack/openflow) - An OpenFlow controller framework in Go.
- [NodeFlow](https://github.com/gaberger/NodeFLow) - An OpenFlow Controller Node Style.
- [NOX](https://github.com/noxrepo/nox) - An open source development platform for C++-based software-defined networking (*SDN*) control applications.
- [OESS](https://github.com/globalnoc/oess) - The Open Exchange Software Suite to configure and control OpenFlow Enabled switches.
- [ONOS](http://onosproject.org) - Open Network Operating System.
- [Open MUL](http://www.openmul.org/openmul-controller.html) - A lightweight SDN/Openflow controller written almost entirely in C from scratch.
- [Open Security Controller](https://www.opensecuritycontroller.org/) - Software-defined security orchestration solution that automates deployment of virtualized network security functions, like next-generation firewall, intrusion prevention systems and application data controllers
- [OpenContrail](https://tungsten.io/opencontrail-is-now-tungsten-fabric/) - A SDN project that utilizes SDN & NFV and provides all the necessary components for network virtualization.
- [OpenDaylight](https://www.opendaylight.org) - OpenDaylight Platform
- [OVN](http://www.openvswitch.org//support/slides/OVN-Vancouver.pdf) - OVN: Open Virtual Network for Open vSwitch
- [POX](https://github.com/noxrepo/pox) - An open source development platform for Python-based software-defined networking (*SDN*) control applications.
- [Ravel](https://github.com/ravel-net/ravel) - A software-defined networking (SDN) controller that uses a standard SQL database to represent the network.
- [Ryu](https://ryu-sdn.org/) - A component-based software defined networking framework.
- [Trema](https://trema.github.io/trema/) - A full-stack, easy-to-use framework for developing OpenFlow controllers in Ruby and C.
- [Vyatta](https://github.com/BRCDcomm/BVC/) - The first commercial Controller built directly from OpenDaylight.

# Simulator/Emulator

- [Containernet](https://github.com/containernet/containernet) - Mininet fork that allows to use Docker containers as hosts in emulated networks
- [EstiNet](http://www.estinet.com/products.php?lv1=13&sn=13) - A world-renowned software tool for network planning
- [MaxiNet](http://maxinet.github.io) - MaxiNet extends the famous Mininet emulation environment to span the emulation across several physical machines. This allows to emulate very large software-defined networks.
- [Mininet](http://mininet.org/) - An Instant Virtual Network on your Laptop (or other PC)
- [ns-3](https://www.nsnam.org/) - A discrete-event network simulator that supports OpenFlow environment.
- [OpenNet](http://github.com/dlinknctu/opennet) - A simulator for software-defined wireless local area network
- [Tinynet](https://github.com/John-Lin/tinynet) - A lightweight instant virtual network for rapid prototyping SDN

# Language

- [Frenetic](https://github.com/frenetic-lang/frenetic) - The Frenetic Programming Language and Runtime System
- [NEMO](https://wiki.onosproject.org/display/ONOS/NEMO+Language) - A domain specific language (DSL) based on abstraction of network models and conclusion of operation patterns.
- [P4](http://p4.org/) - A declarative language for expressing how packets are processed by the pipeline of a network forwarding element such as a switch, NIC, router or network function appliance.
- [POF](https://dl.acm.org/citation.cfm?id=2491190) - Protocol Oblivious Forwarding
- [Pyretic](http://www.frenetic-lang.org/pyretic/) - Pyretic is one member of the Frenetic family of SDN programming languages.

# Library

- [loxigen](https://github.com/floodlight/loxigen) - LoxiGen is a tool that generates OpenFlow protocol libraries for a number of languages.
- [nettle](https://github.com/AndreasVoellmy/openflow) - A Haskell library for working with the OpenFlow protocol.
- [OCaml OpenFlow](https://github.com/frenetic-lang/ocaml-openflow) - A serialization and protocol library for OpenFlow.
- [oflib-node](https://github.com/TrafficLab/oflib-node) - Oflib-node is an OpenFlow protocol library for Node. It converts between OpenFlow wire protocol messages and Javascript objects.
- [openfaucet](https://github.com/rlenglet/openfaucet) - openfaucet is a pure Python implementation of the OpenFlow 1.0.0 protocol, based on Twisted.
- [OpenFlowJ](https://bitbucket.org/openflowj/openflowj) - A Java implementation of low-level OpenFlow packet marshalling/unmarshalling and IO operations.
- [Scapy](http://www.secdev.org/projects/scapy/) - Scapy is a powerful interactive packet manipulation program.

# Test

- [Cbenech](https://github.com/mininet/oflops/tree/master/cbench) - Benchmarking tool for controllers
- [nice-of](https://code.google.com/archive/p/nice-of/) - A tool to test OpenFlow controller application for the NOX controller platform.
- [oftest](https://github.com/floodlight/oftest) - OpenFlow Testing Framework
- [OpenSDNCore](http://www.opensdncore.org/) - Virtualisation Testbed for NFV/SDN Environment.
- [ptf](https://github.com/p4lang/ptf) - A python based dataplane test framework based on unittest.
- [STS](https://ucb-sts.github.com/sts/) - SDN Troubleshooting System, simulates network devices, allowing programmatically test cases generation.

# NFV

- [OPNFV](https://www.opnfv.org) - Accelerating NFV's evolution through an integrated, open platform.

# Overlay Network

- [GENEVE](https://www.redhat.com/en/blog/what-geneve) - What is GENEVE?
- [NVGRE](https://tools.ietf.org/html/draft-sridharan-virtualization-nvgre-00) - NVGRE-Network-Virtualization-using-Generic-Routing-Encapsulation
- [VXLAN](https://en.wikipedia.org/wiki/Virtual_Extensible_LAN) - Virtual Extensible LAN

# Router

- [bgp4r](https://github.com/jesnault/bgp4r) - BGP4R is a ruby library which enables the creation and manipulation of BGP messages. In BGP4R, all well-known BGP constructs are defined in classes.
- [BGPFeeder](https://github.com/BytemarkHosting/bgpfeeder)
- [Bird](http://bird.network.cz/) - The BIRD project aims to develop a fully functional dynamic IP routing daemon primarily targeted on (but not limited to) Linux, FreeBSD and other UNIX-like systems and distributed under the GNU General Public License.
- [FreeRouter](http://freerouter.nop.hu/) - Java-based vRouter
- [FRRouting](https://frrouting.org/) - An IP routing protocol suite for Linux and Unix platforms which includes protocol daemons for BGP4, BGP4+, OSPFv2, OSPFv3, RIPv1, RIPv2, RIPng, PIM-SM/MSDP and LDP as well as very early support for IS-IS, EIGRP and NHRP.
- [gobgp](https://github.com/osrg/gobgp) - GoBGP is an open source BGP implementation designed from scratch for modern environment and implemented in a modern programming language, the Go Programming Language.
- [Quagga](http://www.quagga.net/) - Quagga is a routing software suite, providing implementations of OSPFv2, OSPFv3, RIP v1 and v2, RIPng and BGP-4 for Unix platforms, particularly FreeBSD, Linux, Solaris and NetBSD. Quagga is a fork of GNU Zebra which was developed by Kunihiro Ishiguro.
- [yabgp](https://github.com/smartbgp/yabgp) - YABGP is a yet another Python implementation for BGP Protocol. It can be used to establish BGP connections with all kinds of routers (include real Cisco/HuaWei/Juniper routers and some router simulators like GNS3) and receive/parse BGP messages for future analysis.

# Misc

- [Aether Project](https://www.opennetworking.org/aether/) - the first open source Enterprise 5G/LTE Edge-Cloud-as-a-Service platform (ECaaS).
- [Central Office Re-architected as a Datacenter, CORD](http://opencord.org) - Reference Implementation of a Service Delivery Platform that Provides Cloud Economies and Agility.
- [Mininet Spear Narmox](http://mininet.spear.narmox.com) - A online web service provides a visualization of Mininet Topology
- [Open Network Automation Platform, ONAP](https://www.onap.org/) - Alignment of the two projects creates a harmonized and comprehensive framework for real-time, policy-driven software automation of virtual network functions that will enable software, network, IT and cloud providers and developers to rapidly create new services.
- [Open Source MANO Community, OSM](https://osm.etsi.org/welcome/)
- [OPEN-Orchestrator Project, Open-O](https://www.open-o.org)

# High Performance Network

- [ASAP2](http://www.mellanox.com/blog/2016/12/three-ways-asap2-beats-dpdk-for-cloud-and-nfv/) - The ASAP2 accelerator is built on top of eSwitch NIC hardware, and allows either the entire virtual switch, or significant portions of virtual switch or distributed virtual router (DVR) operations to be offloaded to the Mellanox NIC
- [DPDK](http://dpdk.org/) - DPDK is a set of libraries and drivers for fast packet processing.
- [RDMA](https://en.wikipedia.org/wiki/Remote_direct_memory_access) - Remote direct memory access (RDMA) is a direct memory access from the memory of one computer into that of another without involving either one's operating system. This permits high-throughput, low-latency networking
- [XDP](https://www.iovisor.org/technology/xdp) - XDP or eXpress Data Path provides a high performance, programmable network data path in the Linux kernel as part of the IO Visor Project.
It is designed to run on any processors. The first supported CPU was Intel x86 and it is now extended to IBM POWER and ARM.


# Userspace Network Stack

- [drv-netif-dpdk](https://github.com/rumpkernel/drv-netif-dpdk) - drv-netif-dpdk is a DPDK network interface for rump kernels. The combined result is a userspace TCP/IP stack doing packet I/O via DPDK.
- [f-stack](https://github.com/F-Stack/f-stack) - F-Stack is an user space network development kit with high performance based on DPDK, FreeBSD TCP/IP stack and coroutine API.
- [mTCP](https://github.com/eunyoung14/mtcp) - mTCP is a highly scalable user-level TCP stack for multicore systems. mTCP source code is distributed under the Modified BSD License. For more detail, please refer to the LICENSE. The license term of io_engine driver and ported applications may differ from the mTCP’s.
- [net-next-nuse](https://github.com/libos-nuse/net-next-nuse) - Network Stack in Userspace (NUSE) NUSE allows us to use Linux network stack as a library which any applications can directory use by linking the library. Each application has its own network stack so, it provides an instant virtualized environment apart from a host operating system.
- [nff-go](https://github.com/intel-go/nff-go) - NFF-Go becomes part of DPDK project umbrella under Linux Foundation! Mirror repo can be found here: http://dpdk.org/browse/apps/nff-go/. We will accept patches through DPDK mail-list and standard DPDK contribution process too.

# Analytics

- [Apache Spot](http://spot.incubator.apache.org/) - Community-driven cybersecurity project, built from the ground up, to bring advanced analytics to all IT Telemetry data on an open, scalable platform
- [PNDA](http://pnda.io/) - The scalable, open source big data analytics platform for networks and services.
- [SNAS](http://www.snas.io/) - Streaming Network Analytics System (project SNAS) is a framework to collect, track and access tens of millions of routing objects (routers, peers, prefixes) in real time.

# Resources
## Books

- [DevOps for Networking](https://www.packtpub.com/networking-and-servers/devops-networking)
- [Network Algorithmics：An Interdisciplinary Approach to Designing Fast Networked Devices](https://doc.lagout.org/network/Network%20Algorithmics%20An%20Interdisciplinary%20Approach%20to%20Designing%20Fast%20Networked%20Devices.pdf)
- [Network Programmability and Automation Skills for the Next-Generation Network Engineer](http://shop.oreilly.com/product/0636920042082.do)
- [SDN: Software Defined Networks: An Authoritative Review of Network Programmability Technologies](https://www.oreilly.com/library/view/sdn-software-defined/9781449342425/)
- [SDN网络指南](https://feisky.gitbooks.io/sdn/)(OpenSource Book in Chinese by Pengfei Ni)
- [SDN核心技术剖析和实战指南](http://www.sdnlab.com/book/9480.html)
- [Software Defined Networking with OpenFlow](https://www.packtpub.com/networking-and-servers/software-defined-networking-openflow)
- [圖解OpenFlow](http://www.books.com.tw/products/CN11301942)
- [重构网络-SDN架构与实现](http://www.sdnlab.com/book/18762.html)
- [深度解析SDN: 利益、战略、技术、实践](http://www.sdnlab.com/book/9470.html)
- [软件定义网络:SDN与OpenFlow解析](http://www.sdnlab.com/book/9473.html)

## Paper

- [A Guided Tour of Data-Center Networking](http://static.googleusercontent.com/media/research.google.com/zh-CN//pubs/archive/40404.pdf)
- [A Survey on the Security of Stateful SDN Data Planes](https://ieeexplore.ieee.org/document/7890396)
- [High Performance Datacenter Networks: Architectures, Algorithms, and Opportunities](https://static.googleusercontent.com/media/research.google.com/zh-TW//pubs/archive/37069.pdf)
- [Re-architecting datacenter networks and stacks for low latency and high performance](http://dl.acm.org/citation.cfm?id=3098825)
- [SDN A Comprehensive Survey](https://arxiv.org/pdf/1406.0440.pdf)

## Awesome Posts
- [VXLAN L3应用EVPN，呈现完整overlay网络](https://www.sdnlab.com/19879.html)

---
# 🤝 Contributing

Contributions to improve the project are welcome! Please follow these steps:

```markdown

1. **Create a new branch** for your feature or fix  
   ```bash
   git checkout -b feature/AmazingFeature
   # or
   git checkout -b fix/bug-login-validation
   ```

2. **Make your changes** and stage them  
   ```bash
   git add .
   # or more selectively:
   # git add src/components/Button.py tests/test_button.py
   ```

3. **Commit your changes** with a clear message  
   ```bash
   git commit -m "Add AmazingFeature: implement real-time packet visualization"
   # Good examples:
   # git commit -m "fix: resolve division by zero in bandwidth calculator"
   # git commit -m "docs: update installation instructions for macOS"
   ```

4. **Push your branch** to GitHub  
   ```bash
   git push origin feature/AmazingFeature
   ```

5. **Open a Pull Request**  
   - Go to your repository on GitHub  
   - You should see a yellow banner suggesting to open a PR → click **Compare & pull request**  
   - Fill in a meaningful title and description  
   - Link any related issues (e.g. `Closes #45`)  
   - Request review from `@M-Amin-Wolverine` or other team members

---

## Contribution Guidelines

We welcome contributions of all kinds — bug fixes, new features, documentation, tests, examples, etc.

To maintain high code quality, please follow these guidelines:

- **Code Style**  
  - Follow **PEP 8** for all Python code  
  - Use `black` + `isort` for automatic formatting (recommended)  
  - Maximum line length: 88 characters (black default)

- **Documentation**  
  - Every public function, class, and method **must** have a clear docstring (Google or NumPy style preferred)  
  - Include type hints wherever possible (use `typing` or `from __future__ import annotations`)

- **Testing**  
  - Add or update **unit tests** for new/changed logic (preferably using `pytest`)  
  - Aim for meaningful coverage on core logic (visualization, calculations, data parsing)

- **Documentation & README**  
  - Update `README.md` if you add/remove features, change installation steps, or add new screenshots  
  - Keep example code blocks runnable when possible

- **Commit Messages**  
  Use conventional commit style (optional but appreciated):  
  ```
  feat: add latency heatmap visualization
  fix: correct jitter calculation formula
  docs: improve CONTRIBUTING.md examples
  refactor: extract packet parser to separate module
  ```

---

### 📄 License

This project is licensed under the **MIT License**.  
See the [`LICENSE`](LICENSE.md) file for the full text.

---

### 👥 Core Team

- **M. Amin Khodadadi** — Project Lead & Main Developer  
- **IRIB University** — Faculty of Telecommunications (Student Project)

---

### 📞 Contact & Support

- **GitHub Repository**:  
  https://github.com/M-Amin-Wolverine/IRIB-University-Telecommunications-Networks-Final-Project

- **Issues**:  
  [Report a bug or suggest a feature →](https://github.com/M-Amin-Wolverine/IRIB-University-Telecommunications-Networks-Final-Project/issues/new)

- **Email**:  
  amin.khodadadi1380@gmail.com

---

Thank you for helping make this project better! 🚀

---
<div align="center">
⭐ Star this repository if you find it useful!
IRIB University - Faculty of Telecommunications Engineering
*Academic Year 2026-2027*

</div>

### Project conceived, developed, and maintained by Mohammad Amin Khodadadi

### Last major update: Feb.2026
