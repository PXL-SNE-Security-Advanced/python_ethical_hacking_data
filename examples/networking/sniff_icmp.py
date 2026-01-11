# sniff_icmp.py
# Sniff ICMP packets and display summaries
# How test it: run `icmp_ping.py` in another terminal to generate ICMP packets
# Requires root/administrator privileges to run

from scapy.all import sniff

packets = sniff(count=2, filter="icmp", timeout=20)

for p in packets:
    print(p.summary())
