# extract_ips_from_file.py

import re

ip_regex = r"\b\d{1,3}(?:\.\d{1,3}){3}\b"

with open("example.log", "r", encoding="utf-8", errors="ignore") as f:
    for line in f:
        for ip in re.findall(ip_regex, line):
            print(ip)
