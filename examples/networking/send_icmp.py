# send_icmp.py
# Send ICMP Echo Request packets to
from scapy.all import IP, ICMP, send

packet = IP(dst="8.8.8.8") / ICMP()
send(packet, count=5)
