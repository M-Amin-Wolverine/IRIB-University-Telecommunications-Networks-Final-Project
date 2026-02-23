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
