import socket
# Check if port 80 is open on localhost
# spin up a container with: docker run -d -p 80:80 nginx

socket.setdefaulttimeout(1)

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("127.0.0.1", ))
    print("Port 80 is open")
    s.close()
except:
    print("Port 80 is closed")
