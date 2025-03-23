"""
Dissector module for extracting IP and TCP metadata from raw packets.

- Dynamically handles Ethernet, IP, and TCP header sizes
- Returns structured metadata including offsets and sizes
- Designed for integration with Legit Host DB and entropy engine

Status: MVP version, structure subject to change
"""

import socket
import struct
class PacketDissector():
    
    def calculate_offset(packet: bytes, has_ethernet = True):
    #Ethernet Logic

        offset = 0
        if has_ethernet:
            eth_header_len = 14
            offset += eth_header_len
        else:
            eth_header_len = 0

    #IP Header Logic
        ip_header_start = offset
        ip_header = packet[ip_header_start : ip_header_start + 20]
        iphl = packet[ip_header_start] & 0x0F
        ip_header_length = iphl * 4
        offset += ip_header_length

    #Tcp Header Logic
        tcp_header_start = offset
        tcp_header = packet[tcp_header_start: tcp_header_start + 20]
        tcp_data_offset = (packet[tcp_header_start + 12] >> 4) * 4
        tcp_header_length = tcp_data_offset
        offset += tcp_header_length

        return {
            "eth_header_len" : eth_header_len,
            "ip_header_len" : ip_header_length,
            "tcp_header_len" : tcp_header_length,
            "payload_start" : offset,
            "packet_size" : len(packet)
        }