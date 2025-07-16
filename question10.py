#Jaisen McLean
import dpkt, socket, datetime

"""
This is a program that does not do what the question asks but it 
does take the input from a pcap file and 
presents all the IP address source and
destinations with their time stamp.
"""

with open("network_traffic.pcap", "rb") as f:
    pcap = dpkt.pcap.Reader(f)
    for ts, buf in pcap:
        eth = dpkt.ethernet.Ethernet(buf)
        if not isinstance(eth.data, dpkt.ip.IP):
            continue
        ip = eth.data
        src= socket.inet_ntoa(ip.src)
        dst= socket.inet_ntoa(ip.dst)
        timestamp= datetime.datetime.fromtimestamp(ts)
        print(f" {src}, {dst}, {timestamp}")


