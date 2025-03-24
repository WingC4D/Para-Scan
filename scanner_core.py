
import socket
import struct
import random
from analyzer import Response_Analyzer



local_ip = socket.gethostbyname(socket.gethostname()) # Get Local IP dynamically
target_ip = input("Enter Traget IP Address:")
source_port = 12345
target_port = int(input("Enter Target Port:"))


# Dynamic port 
# Will be changed later to immatate legitimate ports used by the host in normal network behavior
source_port = random.randint(1024, 65535) 
# Creates a socket listenig from 3rd layer upwards-> Makes the socket a raw socket ->  Tells the socket only to handel 
# TCP traffic only
send_sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
send_sock.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
#Enable Socket Options (part of Custom Packet Crafting process)
#IP_HDRINCL -> Tells the OS the User is Handling the IP Header Manually
send_sock.settimeout(3) #time out in secs for response

listen_sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))


#IP Header (Manually Constructed)
ip_header = struct.pack(
    "!BBHHHBBH4s4s",
    69, 
    0, 
    40,
    54321, 
    0, 
    255, 
    socket.IPPROTO_TCP, 0,
    socket.inet_aton("127.0.0.1"), #Manually Spoofed Source IP if not set to "local_ip" or socket.gethostbyname.(socket.gethostname())
    socket.inet_aton(target_ip)
)

#TCP Header (SYN packet)
tcp_header = struct.pack(
    "!HHLLBBHHH",
    source_port,  # Random Source Port
    target_port,  # Destination Port
    0, 0,         # Sequence & Acknowledgment Number
    80, 2,        # Data Offset, SYN flag
    64240, 0, 0   # Window size, Checksum (will be calcculated), Urgent pointer
)

#sends the packet
send_sock.sendto(ip_header+ tcp_header, (target_ip, 0))
print(f"Sent a TCP SYN Packet to IP Address: {target_ip}, Port: {target_port}")

# Capture and Analyze the Response
Response_Analyzer.receive_response(listen_sock, target_port)