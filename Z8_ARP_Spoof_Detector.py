#!/usr/bin/env python

import scapy.all as scapy
 


def sniff(interface):
	# we run the sniff function so that we can get a ARP response 
	scapy.sniff(iface=interface, store=False, prn=porcess_sniffed_packet) 


def get_mac(ip):
	# get_mac will get us the mac address of the provided ip address
	arp_request = scapy.ARP(pdst = ip)
	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	arp_request_broadcast = broadcast / arp_request
	answered_list = scapy.srp(arp_request_broadcast, timeout=1 ,verbose=False)[0]
	return answered_list[0][1].hwsrc  

def porcess_sniffed_packet(packet):
	if packet.haslayer(scapy.ARP) and packet[scapy.ARP].op == 2:  # It'll check for the ARP packet layer which is 'is at' response
		# print(packet.show())
		try:
			real_mac = get_mac(packet[scapy.ARP].psrc)  # now this will get us the mac addreess of router using it's ip
			response_mac = packet[scapy.ARP].hwsrc  # and this is the response mac address we're actually getting from the ARP packet

			if real_mac != response_mac:  # now this will check the if the real_mac and response mac is same or not
				print("[*] Possible ARP spoof Attack")
			else:
				print("[*] No ARP spoof Attack detected")

		except Exception:
			print("[-] There seem to be an error")


		


sniff("eth0")