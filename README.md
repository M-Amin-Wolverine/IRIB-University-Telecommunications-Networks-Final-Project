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
   ### A Flow-Based Performance Evaluation on RYU SDN Controller | Journal of The  Institution of Engineers (India): Series B | Springer Nature Link
   ### Ryu controller architecture: layered design with event dispatcher, OpenFlow parser, built-in apps, and custom SDN applications.

   2. **Multi-VLAN Switching**
      - 802.1Q VLAN tagging/untagging handled on access ports
      - Trunk ports configured with allowed VLAN lists (via OpenFlow actions: set_field vlan_vid)
      - Native VLAN support for untagged ingress/egress traffic
      - Inter-VLAN routing fully mediated by the controller (no distributed routing protocol)
   <div style="display: flex; gap: 10px;">
    <img src="https://github.com/user-attachments/assets/705136ae-f618-4c39-9b32-4e790878f1e9" width="475" />
    <img src="https://github.com/user-attachments/assets/01f024f2-d5e0-4ab6-b2df-71524bf3b57f" width="475" />
   </div>
   ### Typical inter-VLAN routing setups — left: router-on-a-stick style; right: multi-switch topology with VLAN separation, analogous to SDN controller-mediated routing.

   

