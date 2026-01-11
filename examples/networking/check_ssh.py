# Check if SSH is running on localhost
import socket

def is_port_open(host, port):
    try:
        socket.create_connection((host, port), timeout=1)
        return True
    except:
        return False

if is_port_open("127.0.0.1", 22):
    print("SSH detected")
