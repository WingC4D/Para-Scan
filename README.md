# ParaScan  
**Advanced Internal Port Scanning and Traffic Simulation Tool**

ParaScan is an advanced Linux-only port scanning and behavioral emulation tool designed to simulate realistic TCP conversations and evade both signature-based and behavioral detection systems. It rotates device identity (IP/MAC), mimics application flows, and avoids traditional scanning fingerprints by blending into internal network traffic.

---

## 📌 Overview

ParaScan is built for internal reconnaissance, stealth port analysis, and host impersonation. It simulates legitimate traffic patterns, uses entropy-driven obfuscation, and supports red team and adversary simulation exercises. The tool is modular and under active development, with planned support for traffic replay, decoy injection, and detection analysis.

This is a personal learning project focused on offensive security, protocol manipulation, and stealth behavior modeling.

---

## 🎯 Core Design Features

| Feature | Purpose |
|--------|---------|
| ✅ TCP Completeness Evasion | Craft full or partial TCP flows to avoid behavioral signatures |
| ✅ DHCP Network Mapping Tool | Sends a single DISCOVER to map internal subnets, gateways, and DNS |
| ✅ Passive Packet Analyzer | Dissects incoming packets to determine port status without active noise |
| ⏳ Chaotic IP Spoofer | Rotates spoofed internal IPs using entropy-based logic |
| ⏳ Chaotic MAC Spoofer | Uses AF_PACKET to spoof MAC addresses and simulate different LAN devices |
| ⏳ DNS Response Spoofer (*loud*) | Responds to internal DNS queries for redirect or payload injection |
| ⏳ DHCP Response Spoofer (*persistence*) | Offers rogue DHCP configurations to persist on target networks |
| ⏳ Decoy Traffic Injection | Sends realistic but fake traffic to populate logs or cover real activity |

---

## 🧠 Behavior Simulation Scope

This tool is designed to:

- Simulate complete TCP conversations, including payload exchange and teardown
- Rotate TCP fingerprint traits (TTL, window size, options)
- Operate non-linearly with randomized timing to avoid correlation
- Blend in with real LAN traffic for long-dwell stealth operations
- Function independently of scanning tools like Nmap or Scapy

---

## 🔨 Modules (Current + Planned)

- `scanner_core.py` – SYN scanner with flow emulation
- `analyzer.py` – TCP/IP packet analysis and response classification
- `profile_db.py` – TCP fingerprint profiles (TTL, WS, flags)
- `mapper_dhcp.py` – Subnet discovery using DHCP
- `mac_tools.py` – MAC address spoofing (planned)
- `dns_spoofer.py` – Internal DNS redirection (planned)
- `dhcp_spoofer.py` – Rogue DHCP injection (planned)
- `decoy_injector.py` – Simulated traffic replayer (planned)

---

## 🧱 Roadmap Phases

**Phase 1 – Core Tools**  
- [x] SYN scanner (raw)
- [x] Packet dissector
- [x] DHCP discover
- [x] Passive sniffer

**Phase 2 – Stealth**  
- [x] IP spoofing from internal IP pool  
- [ ] TTL/window/flag randomizer  
- [ ] MAC spoofing via AF_PACKET  

**Phase 3 – Traffic Profiles**  
- [ ] TCP conversation generator  
- [ ] Payload emulation engine  
- [ ] Timing templates per profile  

**Phase 4 – Detection Support**  
- [ ] Passive detection mode  
- [ ] CLI mode toggles  

**Phase 5 – DNS/DHCP Spoofing**  
- [ ] DNS responder for injection  
- [ ] DHCP rogue server  

**Phase 6 – Decoy Engine**  
- [ ] Legitimate session replay  
- [ ] Decoy traffic injection

---

## 📎 Requirements

- Linux / WSL2  
- Python 3.11+  
- Root privileges for raw sockets / AF_PACKET

---

## ⚠️ Disclaimer

This project is for ethical red team simulation, network defense training, and protocol behavior study.  
Do not use on networks you are not authorized to test.
# WingC4D
