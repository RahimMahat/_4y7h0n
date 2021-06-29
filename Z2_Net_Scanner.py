#!usr/bin/env python

import scapy.all as scapy  #this module only works with python3 and not with python2

def scan(ip):
	# i. Creating a ARP request directed to broadcast MAC asking for ip:
	arp_request = scapy.ARP(pdst = ip)  # pdst is func. we get to set target ip address after we run scapy.ls
	# print(arp_request.summary())
	# scapy.ls(scapy.ARP())  # to get the functions that we can use in scapy.ARP class to set the target ip address 

	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") # this will create an ethernet object  and dst is func we got from scap.ls
	# print(broadcast.summary())
	# scapy.ls(scapy.Ether())

	arp_request_broadcast = broadcast / arp_request # combining the arp_request and broadcast
	# print(arp_request_broadcast.summary())
	# arp_request_broadcast.show()  # this will show the detailed result of ARP + Broadcast packet


	# ii. Send packet and receive response:
	# answered_list,unanswered_list = scapy.srp(arp_request_broadcast, timeout=1) # srp is func. which will allow us to send and recieve packets with custom ethernet that we create above
	# after sending srp to the given ip range you'll get couple of list of answered and unanswered packets so we capture that differently
	answered_list = scapy.srp(arp_request_broadcast, timeout=1 ,verbose=False)[0] # to only get the content of answered packets
	# print(answered_list.summary())						  # verbose=False will give you less detailed output for pretty printing

	# iii. Parsing the response that we got:
	# for element in answered_list:
		# print(element[1].show())  # in this psrc and hwsrc will contain the ip and MAC address of responded network
		# elment[1] contains the info of packet
		# print(element[1].psrc)
		# print(element[1].hwsrc)
		# print("-------------------------------------------------------------------------------------------")  # to seperate each element

	# iv. Pretty printing the result:
	print("-----------------------------------")
	print("IP\t\t  MAC Address")
	print("-----------------------------------")
	for element in answered_list:
		print()
		print(element[1].psrc+"\t"+element[1].hwsrc)
		print()
		


IP_range = input("Enter the IP range to find networks: ")

scan(IP_range)












# simple script
'''
def scan(ip):
	scapy.arping(ip)

scan("10.0.0.1/24")  # The range of ip address Eg. from 10.0.0.1 to 10.0.0.254
'''
