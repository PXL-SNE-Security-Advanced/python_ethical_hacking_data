import socket

# Grab banner from scanme.nmap.org on port 80
s = socket.socket()
# connect to scanme.nmap.org
s.connect(("scanme.nmap.org", 80))
# send HTTP HEAD request
s.send(b"HEAD / HTTP/1.0\r\n\r\n")
banner = s.recv(1024)
# print banner, ignoring decode errors
print(banner.decode(errors="ignore"))
s.close()
