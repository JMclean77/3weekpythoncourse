import socket

def is_valid_ip(ip):
    parts = ip.strip().split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit():
            return False
        num = int(part)
        if not (0 <= num <= 255):
            return False
    return True

def is_valid_port(port):
    try:
        port = int(port)
        return 1 <= port <= 65535
    except:
        return False

# Test cases
ips = ["128.0.0.1", "125.16.100.1", "125.512.100.1", "125.512.100.abc", "19212801"]

for ip in ips:
    print(f"{ip} -> Valid: {is_valid_ip(ip)}")

print(f"Port 80 valid? {is_valid_port('80')}")
print(f"Port 70000 valid? {is_valid_port('70000')}")


import socket

def scan_ports(ip):
    socket.setdefaulttimeout(1)  # 1 second timeout
    print(f"Scanning ports 1 to 100 on {ip}...\n")

    for port in range(1, 101):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            result = s.connect_ex((ip, port))  # 0 = open, anything else = closed
            if result == 0:
                print(f"Port {port} is OPEN")


scan_ports("8.8.8.8")
