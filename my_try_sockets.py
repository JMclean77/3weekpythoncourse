import socket
import ipaddress


def is_ip_valid(ip):
    parts= ip.strip().split(".")
    if len(parts) != 4:
        return False
    for part in parts:
        if int(part) < 0 or int(part) > 255:
            return False
    return True

def is_valid_port(port):
    try:
        port = int(port)
        if port < 0 or port > 65535:
            return False
        return True
    except ValueError:
        return False

ips= ["128.0.0.1", "125.16.100.1", "125.512.100.1", "125.512.100.abc", "19212801"]

for ip in ips:
    if is_ip_valid(ip):
        print(f"{ip}  Valid: {is_ip_valid(ip)}")
    else:
        print(f"{ip}  valid: {is_ip_valid(ip)}")

print(f"is port 80 valid? {is_valid_port(80)}")
print(f"is port 443 valid? {is_valid_port(443)}")
print(f"is port 70252 valid? {is_valid_port(70252)}")


def scan_ports(ip):
    socket.setdefaulttimeout(1)
    print(f"Scanning ports...")

    for port in range(22, 180):
        with (socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
            result= sock.connect_ex((ip, port))
            if result == 0:
                print(f"Port {port} is OPEN")
            else:
                print(f"Port {port} is CLOSED")

            sock.close()


scan_ports("127.0.0.1")
