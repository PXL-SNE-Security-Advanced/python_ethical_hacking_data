# icmp_ping.py
from scapy.all import IP, ICMP, sr1

packet = IP(dst="8.8.8.8") / ICMP()
reply = sr1(packet, timeout=2, verbose=False)

if reply:
    print("Host responded")
else:
    print("No response")

# Display packet summary
reply.summary()

# Display detailed packet information
reply.show()
