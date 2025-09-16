import socket
import sys

if len(sys.argv) < 3:
    print("Usage: python script.py <host> <port>")
    sys.exit(1)

host = sys.argv[1]
port = int(sys.argv[2])


def is_port_in_use(port, host='127.0.0.1'):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex((host, port)) == 0

# Usage Example:
if is_port_in_use(port, host):
    print(f"Port {port} is in use on {host}")
else:
    print(f"Port {port} is free on {host}")
