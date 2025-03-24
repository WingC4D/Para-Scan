import socket
import struct
from tcp_flags import *
from dissector import PacketDissector

class Response_Analyzer:
    def receive_response(sock, target_port):
        try:
        # Step 1: Receive packet, (65535 is the maxium amount of bytes we can recive).
            response,  addr = sock.recvfrom(65535) 
        #!!! ^this^ captures the raw socket !!!
            print(f"[*] Received a response from {addr}: {response.hex()}") 
        # Step 2: Dissect it
            dissector = PacketDissector()
            resp_valu_dict = dissector.calculate_offset(response)
            
            eth_header = resp_valu_dict["ethernet_header"]
            dst_mac = eth_header[:6]
            src_mac = eth_header[6:12]
            eth_type = struct.unpack("!H", eth_header[12:14]) [0]

        # Step 4 Extract the IP header as a Byte obj. !!!
            ip_header = resp_valu_dict['ip_header'] #Extracts the first 20 bytes
        
        
            ip_hdr = struct.unpack("!BBHHHBBH4s4s", ip_header)
        
        
            protocol = ip_hdr[6] # Extract Protocol for (should be 6 for TCP)


            if protocol == 6: #TCP Packet
                tcp_header = resp_valu_dict['tcp_header'] # Extract the next 20 bytes of the Response (The TCP Header) 
            # !!! ^This^ is a BYTE obj. !!!
            
                tcp_hdr = struct.unpack("!HHLLBBHHH", tcp_header) #Decoding the Bytes into a packet
            # !!! ^this^ is a tuple containting the packet as a string obj. !!!

                source_port = tcp_hdr[0]
                dst_port = tcp_hdr[1]
                flags = tcp_hdr[5] 

            
                if flags == 0x12: # SYN-ACK
                    print(f"Port {dst_port} is OPEN (Recived a  SYN-ACK packet)")
                elif flags == 0x04: # RST
                    print(f"Port {dst_port} is CLOSED (Recived a RST packet)")
                else: # Everything else
                    print(f"Unplanned Response Flags: {TCP_flags[flags]}")
        
        
        except socket.timeout:
            print(f"!!! Port {target_port} is FILTERED (no response, you MAY BE CAUGHT)")