import nmap

nmScan = nmap.PortScanner()

nmScan.scan('127.0.0.1', '21-443')


# Shows the exact nmap command used
print(nmScan.command_line())

# Lists all scanned hosts
print(nmScan.all_hosts())

# Get the hostname of 127.0.0.1
print(nmScan['127.0.0.1'].hostname())

# Get the host state (e.g. 'up' or 'down')
print(nmScan['127.0.0.1'].state())

# List all detected protocols (e.g. ['tcp'])
print(nmScan['127.0.0.1'].all_protocols())

# Get keys under a protocol (usually ports)
print(nmScan['127.0.0.1']['tcp'].keys())

# Check if a host has TCP protocol info
print(nmScan['127.0.0.1'].has_tcp(22))

# Get specific port info for TCP port 22 (usually SSH)
if 22 in nmScan['127.0.0.1']['tcp']:
    print(nmScan['127.0.0.1']['tcp'][22])
else:
    print("Port 22 is not open or found")

