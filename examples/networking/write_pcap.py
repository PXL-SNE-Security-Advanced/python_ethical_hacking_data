# write_pcap.py
from scapy.all import sniff, wrpcap

packets = sniff(count=20, timeout=10)
wrpcap("capture.pcap", packets)
