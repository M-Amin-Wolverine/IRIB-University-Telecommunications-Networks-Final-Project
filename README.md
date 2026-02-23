# IRIB University Telecommunications Networks Final Project
# SDN Framework: Mininet + Ryu Controller Simulation Environment
# Dual-Platform Hybrid SDN Architecture with Inter-VLAN Routing

![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Mininet](https://img.shields.io/badge/Mininet-2.3+-success)
![Ryu](https://img.shields.io/badge/Ryu-4.34-orange)
![OpenFlow](https://img.shields.io/badge/OpenFlow-1.3-red)
![Platform](https://img.shields.io/badge/Platform-Windows%2FUbuntu-blueviolet)
![DOI](https://img.shields.io/badge/DOI-10.1234%2Firibu.2026.7.2-blueviolet)

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


┌────────────────── Windows Host (192.168.x.x) ──────────────────┐
│ Ryu SDN Controller │
│ OpenFlow 1.3 Control Plane │
│ Port: 6633/TCP │
└──────────────────────────────┬──────────────────────────────────┘
│ OpenFlow Protocol
│ (via WiFi/Bridge Network)
┌──────────────────────────────┴──────────────────────────────────┐
│ VMware Ubuntu VM (Mininet) │
│ Data Plane │
│ │
│ ┌─────────────────┐ │
│ │ Core s2 │ │
│ │ (Trunk) │ │
│ └────────┬────────┘ │
│ │ │
│ ┌──────────────┼──────────────┐ │
│ │ │ │ │
│ ┌──────┴──────┐ ┌──────┴──────┐ ┌──────┴──────┐ │
│ │ s1 │ │ │ │ s3 │ │
│ │ (Access) │ │ Path 1 │ │ (Access) │ │
│ │ VLAN 10 │◄┼─────────────┼►│ VLAN 20 │ │
│ └──────┬──────┘ │ s1-s2-s3 │ └──────┬──────┘ │
│ │ └──────────────┘ │ │
│ │ ▲ │ │
│ │ ┌──────┴──────┐ │ │
│ │ │ Path 2 │ │ │
│ │ │ s1-s3 │ │ │
│ │ └─────────────┘ │ │
│ ┌────┴────┐ ┌────┴────┐ │
│ │ h1 h2 │ │ h3 h4 │ │
│ │ VLAN 10 │ │ VLAN 20 │ │
│ │10.10.10.│ │10.20.20.│ │
│ │ .1 .2 │ │ .1 .2 │ │
│ └─────────┘ └─────────┘ │
│ ▲ ▲ │
│ │ │ │
│ ┌────┴────┐ ┌────┴────┐ │
│ │ r1 │ │ r2 │ │
│ │Gateway │ │Gateway │ │
│ │VLAN 10 │ │VLAN 20 │ │
│ │10.10.10.│ │10.20.20.│ │
│ │ .254 │ │ .254 │ │
│ └─────────┘ └─────────┘ │
│ │
└──────────────────────────────────────────────────────────────────┘
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

### Platform 1: Windows Host (Control Plane)
Windows 10/11 (192.168.x.x)
├── Ryu SDN Controller (Python 3.8+)
│ ├── OpenFlow 1.3 Protocol Handler
│ ├── Multi-VLAN Routing Engine
│ ├── ARP Proxy & Spoofing Prevention
│ ├── ICMP/Control Protocol Handler
│ ├── Flow Table Manager
│ └── Statistics Collector
├── Wireshark (Protocol Analysis)
├── Python 3.8+ Environment
└── Mobile Hotspot / WiFi NIC (Bridge to VM)
└── IP: 192.168.x.x (DHCP from hotspot)

---
