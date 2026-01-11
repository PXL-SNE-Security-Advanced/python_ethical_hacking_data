# arp_request.py
from scapy.all import ARP, Ether, srp

# Create ARP request packet
# Broadcast MAC address to all devices in the subnet.
# Who has 192.168.0.100?” You can use your own subnet here.
packet = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst="192.168.0.100/24")
answered, unanswered = srp(packet, timeout=2, verbose=False)

for sent, received in answered:
    print("IP:", received.psrc, "MAC:", received.hwsrc)
