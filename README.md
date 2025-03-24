# ParaScan

ParaScan is a simple educational TCP port scanner built using raw sockets. It is part of a personal learning project focused on understanding how packets behave on the network, how systems respond, and how to dissect raw data at the Ethernet, IP, and TCP layers.

This tool is not designed for production use. It's a playground for experimenting with low-level network logic and stealth concepts in a controlled, responsible environment.

---

## 📌 Features (Current MVP)
- Sends manually crafted TCP SYN packets using raw sockets (IPv4)
- Captures full Ethernet frames from the network (L2)
- Dynamically dissects Ethernet, IP, and TCP headers
- Analyzes TCP flags to determine port state (e.g., SYN-ACK, RST)
- Logs raw response data and header details for inspection

---

## 🧪 Current Use Case
- Designed to scan a single target IP and port interactively
- Educational tool for learning how real packet structures look and behave
- Response analysis includes MAC extraction, TCP flag evaluation, and protocol filtering

---

## ⚙️ Requirements
- Python 3.10+
- Linux (AF_PACKET sockets used for L2 sniffing)
- Root privileges to open raw sockets

---

## 🚧 Future Learning Goals
- Add support for scanning multiple ports and ranges
- Integrate TTL, Window Size, and TCP Option fingerprinting
- Add entropy-based traffic shaping for stealth experiments
- Structure a Legitimate Host Behavior DB for adversary simulation

---

## 🛑 Disclaimer
This tool is for educational and ethical research purposes **only**.  
Do not scan systems or networks you do not own or have explicit permission to analyze.

---

## 📂 Repo Structure
- `scanner_core.py`: Sends crafted packets and controls the scan
- `analyzer.py`: Receives and dissects incoming packets
- `dissector.py`: Handles dynamic extraction of Ethernet, IP, and TCP headers
- `tcp_flags.py`: Basic TCP flag reference table

---

Maintained by [WingC4D](https://github.com/WingC4D).

