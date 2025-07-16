# import csv
#
# import dpkt
# import socket
# import datetime
# import pandas as pd
#
# def print_pcap(pcap, writer):
#     packet_counter= 0
#     for (ts,buf) in pcap:
#         try:
#             eth = dpkt.ethernet.Ethernet(buf)
#             ip = eth.data
#             src = socket.inet_ntoa(ip.src)
#             dst = socket.inet_ntoa(ip.dst)
#             prto= ip.p
#             timestamp= datetime.datetime.fromtimestamp(ts)
#
#             packet_counter += 1
#             packets= f"Packet Counter: {packet_counter} | Source: {src} | Destination: {dst} | Timestamp: {timestamp} | Protocol: {prto}"
#             print(packets)
#             writer.writerow([packet_counter, src, dst, timestamp, prto])
#
#         except:
#             pass
#
#
# def main():
#     f= open("file05.pcap", "rb")
#     pcap = dpkt.pcap.Reader(f)
#     with open("pcap.csv", "w", newline= '') as f:
#         writer = csv.writer(f)
#         packet.show()writer.writerow(["Packet Counter", "Source", "Destination", "Timestamp", "Protocol"])
#         print_pcap(pcap, writer)
#
#
# main()

import scapy