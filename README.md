# lan-ip-packet-sniffer
This project is a Python-based LAN traffic monitoring tool designed to capture and analyze IP packets on a local network interface.

## Objectives
- Capture IPv4 and IPv6 packets
- Extract source and destination IP addresses
- Identify transport protocols (TCP, UDP, ICMP)
- Compute simple traffic statistics
- Display a live packet stream

## Technologies
- Python
- Scapy

## Project Structure
```
lan-ip-packet-sniffer/
│
├── main.py          # Entry point
├── sniffer.py       # Packet capture logic
├── parser.py        # IP packet parsing
├── stats.py         # Traffic statistics
├── requirements.txt # Dependencies
└── README.md        # Documentation
```
