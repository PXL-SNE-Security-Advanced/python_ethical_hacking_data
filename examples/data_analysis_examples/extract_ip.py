# extract_ip.py
import re

line = "Failed password for admin from 10.0.0.5 port 55221"
# explanation: \d+ = digits, \. = dot, + means repeat one or more times
match = re.search(r"(\d+\.\d+\.\d+\.\d+)", line)

if match:
    print("IP:", match.group(1))
