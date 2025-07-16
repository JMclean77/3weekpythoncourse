from scapy.layers.inet import *
from scapy.all import *

# Build a basic packet to test with
packet = IP(dst="8.8.8.8")/TCP(dport=80, flags="S")

# Send the packet and receive a reply (if any)
response = sr1(packet, timeout=10, verbose=0)

if response:
    print("\n=== nsummary() ===")
    packets = [response]
    for i, pkt in enumerate(packets):
        print(f"{i}: {pkt.summary()}")  # similar to nsummary()

    print("\n=== summary() ===")
    print(response.summary())

    print("\n=== hexdump() ===")
    hexdump(response)

    print("\n=== show() ===")
    response.show()

    print("\n=== show2() ===")
    response.show2()

    print("\n=== rawhex() ===")
    print(raw(response).hex())  # rawhex isn't a direct function, this is equivalent
else:
    print("No response received.")
