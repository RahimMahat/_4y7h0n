#!usr/bin/env python

import scapy.all as scapy
import argparse

def get_argumets():
	parser = argparse.ArgumentParser()
	parser.add_argument("-t","--target", dest="target", help="Target IP or IP range")
	options = parser.parse_args()
	return options

def scan(ip):
	arp_request = scapy.ARP(pdst = ip)
	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	arp_request_broadcast = broadcast / arp_request
	answered_list = scapy.srp(arp_request_broadcast, timeout=1 ,verbose=False)[0]

	
	capNet_list = []
	for element in answered_list:
		capNet_dict = {"ip" : element[1].psrc, "mac" : element[1].hwsrc}
		capNet_list.append(capNet_dict)

	return capNet_list

def print_result(results_list):
	print("-------------------------------------------------------")
	print("        IP\t\t\tMAC Address")
	print("-------------------------------------------------------")
	for networks in results_list:
		print(networks["ip"] +"\t\t    "+ networks["mac"])


options = get_argumets()
Scanned_Networks = scan(options.target)
print_result(Scanned_Networks)