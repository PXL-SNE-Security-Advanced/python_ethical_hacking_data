# sniff_packets.py
from scapy.all import sniff

packets = sniff(count=10, timeout=10)
print("Captured packets:", len(packets))
