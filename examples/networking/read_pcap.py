# read_pcap.py
from scapy.all import rdpcap

packets = rdpcap("capture.pcap")
print("Total packets:", len(packets))

for p in packets[:5]:
    print(p.summary())
