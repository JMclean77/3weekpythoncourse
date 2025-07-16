from scapy.layers.inet import *
from scapy.all import *


def send_tcp_packet(target_ip, target_port):
    """
    Sends a TCP SYN packet to the target IP and port.
    Prints out whether the port is open, closed, or not responding.
    """


    ip_layer = IP(dst=target_ip)

    # Create a TCP packet with the destination port and SYN
    tcp_layer = TCP(dport=target_port, flags='S')

    print(f"[+] Sending TCP SYN to {target_ip}:{target_port}")

    # Send the packet and wait for a reply
    response = sr1(ip_layer / tcp_layer, timeout=2, verbose=0)

    # If we get a response, analyze it
    if response:
        print("[+] Response received:")
        print(f"    Flags: {response[TCP].flags}")  # Show the TCP flags from the response

        # If we get SYN+ACK, the port is open
        if response[TCP].flags == "SA":
            print("    Port is likely OPEN (SYN-ACK received).")

        # If we get RST+ACK, the port is closed
        elif response[TCP].flags == "RA":
            print("    Port is CLOSED (RST-ACK received).")

        # Any other flags are unexpected
        else:
            print("    Unexpected response.")
    else:
        # No response means the port might be filtered or the host is down
        print("[-] No response received (Filtered or Host Down).")


# This block runs when the script is launched directly
if __name__ == "__main__":
    # Check if user gave both IP and port as arguments
    if len(sys.argv) != 3:
        print("Usage: sudo python3 assignment13_tcp_scapy.py <target_ip> <target_port>")
        sys.exit(1)

    # Save the inputs into variables
    target_ip = sys.argv[1]
    target_port = int(sys.argv[2])

    # Call the function to send the TCP packet
    send_tcp_packet(target_ip, target_port)
