# 🎭 Stealth Strategy — ParaScan

This document outlines the stealth and obfuscation strategies implemented or planned in ParaScan. Each tactic is based on realistic attacker behavior observed in internal recon operations and is designed to reduce the scanner’s detectability by IDS, IPS, or EDR systems.

The goal is to simulate a paranoid, slow-moving adversary who avoids threshold-based detection, signature triggers, and behavioral anomalies.

---

## ✅ Objectives

- Blend with legitimate internal traffic
- Avoid detection based on packet headers, timing, and sequence patterns
- Obfuscate both device identity and traffic origin
- Introduce misdirection and false positives (decoys)
- Support adversary simulation for red/blue training and detection engineering

---

## 1. TCP Completeness Evasion

**Status:** Implemented  
**Purpose:** Avoid detection based on missing or abnormal TCP flows

- Sends SYN packets with legitimate TTL, WS, flags and options
- Can complete full handshake or simulate teardown
- Optional PSH/ACK phase with valid-looking  (not yet implemented)
- Avoids common detection rules like:
  - “SYNs without ACKs”
  - “Too many incomplete connections”
  - “No application-layer activity”

---

## 2. DHCP Mapping (Passive Subnet Discovery)

**Status:** Implemented  
**Purpose:** Discover LAN layout without scanning

- Sends a single `DHCPDISCOVER`
- Extracts IP range, default gateway, and internal DNS
- Quieter than ARP sweep, nmap, or netdiscovery
- Allows scanner to blend in with legitimate client behavior

---

## 3. Passive Packet Analyzer

**Status:** Implemented  
**Purpose:** Port mapping without active polling

- Listens for unsolicited SYN-ACK/RST packets
- Analyzes responses without transmitting follow-up packets
- Enables passive classification of port state after spoofed scans
- No need to expose real host identity during analysis

---

## 4. IP Spoofing (Entropy-Based)

**Status:** Planned  
**Purpose:** Obfuscate source identity and avoid correlation

- Pulls internal IPs from DHCP or observed traffic
- Applies entropy-based rotation logic (non-linear, randomized)
- Prevents correlation between spoofed IPs and packet timing
- Avoids signature detection from IDS/IPS based on consistent scan origin

---

## 5. MAC Spoofing (Entropy-Based)

**Status:** Planned  
**Purpose:** Simulate different internal hosts at Layer 2

- Uses AF_PACKET to craft Ethernet headers
- Randomizes source MAC addresses with real vendor prefixes
- Paired with IP spoofing for full host impersonation
- Intended to defeat basic MAC-IP correlation in ARP logs or NAC systems

---

## 6. DNS Response Spoofer

**Status:** Planned  
**Purpose:** Enable redirection or payload delivery via DNS

- Listens for LAN DNS queries
- Responds with attacker-controlled IP for selected hostnames
- Used for:
  - Simulated phishing/C2 callback
  - Internal browser injection simulation
  - File/payload redirection

> **Note:** High risk of detection. Designed for noisy ops or distraction layers.

---

## 7. DHCP Response Spoofer

**Status:** Planned  
**Purpose:** Persistence via rogue network config

- Responds to DHCPDISCOVER packets with fake gateway/DNS info
- Can redirect victims to attacker-controlled DNS/web servers
- Enables extended presence on victim device or environment
- Can be combined with DNS spoofing for deeper impact

> **Note:** High-risk, targeted for simulated post-exploitation scenarios

---

## 8. Decoy Traffic Injection

**Status:** Planned  
**Purpose:** Obfuscate recon behavior and populate logs

- Sends legitimate-looking TCP sessions (with teardown)
- Mimics known services (HTTP, SMB, etc.) using profile templates
- Pollutes logs with fake-but-clean data
- Forces defenders to waste time triaging false positives

> **Bonus:** Can be used to generate cover traffic during actual recon

---

## 🔐 Detection Evasion Summary

| Threat Model | Mitigated |
|--------------|-----------|
| Signature-based IDS | ✅ via header obfuscation, flag emulation |
| Behavioral detection | ✅ via traffic shaping and legit flow simulation |
| Host/IP correlation | ✅ via IP + MAC spoofing |
| Volume-based anomaly | ✅ via entropy-based timing + pacing |
| DNS/DHCP detection | ⚠️ Only partially mitigated (high noise ops) |

---

## 🧠 Strategic Notes

- Every feature is modular and can be toggled per operation
- Obfuscation is layered — identity, behavior, and timing
- Tool is not silent — it is *plausible*
- Target use case is long-dwell internal recon or red team training simulation
- Logging and detection support are planned for defender integration

---

*Last updated: March 2025*
