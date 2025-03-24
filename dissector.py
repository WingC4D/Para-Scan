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
    
    def calculate_offset(self, packet: bytes, has_ethernet = True):
    #bytes counter for Layer saperation
        offset = 0
    # --- Ethernet Header Logic ---
    # Ethernet header is typically 14 bytes.
    # If no Ethernet header, offset stays 0.
        eth_header_len = 14 if has_ethernet else 0 
        if has_ethernet:
    #Corrupot Frames FIltering logic
            if len(packet) < eth_header_len:
                raise ValueError("Packet Is Too Small For Ethernet")
        
            offset += eth_header_len


    # --- IP Header Logic ---
        ip_header_start = offset
        min_ip_header_len = 20 # Minimum IP header size
    # Ensure packet is large enough for minimum IP header
        if len(packet) < ip_header_start + min_ip_header_len:
            raise ValueError("Packet Too Small To Be An IP Header")
    # iphl = Internet Header Length, lowest 4 bits of the first byte of IP header    
        ihl = packet[ip_header_start] & 0x0F # 0x0f bainary for 0000 1111 therefore leaving only the IHL
    #IP header length (ip_header_length) = iphl multiplied by 4 bytes
        ip_header_length = ihl * 4
    #Corrupot Packet FIltering logic
        if len(packet) < ip_header_start + ip_header_length:
            raise ValueError("Packet Too Small For IP Header Length Specified")
        
        offset += ip_header_length

    
    #--- TCP Header Logic ---
        tcp_header_start = offset
        min_tcp_header_len = 20
        if len(packet) < tcp_header_start + min_tcp_header_len:
            raise ValueError("Packet Too Small For Minimum TCP Header")
        
        tcp_data_offset = (packet[tcp_header_start + 12] >> 4) * 4
        tcp_header_length = tcp_data_offset
        
        offset += tcp_header_length
    # --- Correctly separated headers and payload ---
        packet_dict = {
            "ethernet_header " : packet[0 : eth_header_len],
            "ip_header" : packet[eth_header_len : eth_header_len + ip_header_length],
            "tcp_header" : packet[eth_header_len + ip_header_length : eth_header_len + ip_header_length + tcp_header_length],
            "payload" : packet[offset : ],
            "packet_size" : len(packet)
        }
        
        return packet_dict
