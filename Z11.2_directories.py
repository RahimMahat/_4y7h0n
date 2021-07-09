#!/usr/bin/env python

import requests


def request(url):
	try:
		return requests.get("http://" +url)
	except requests.exceptions.ConnectionError:
		pass

target_url = "localhost/mutillidae"

with open("small-filesNdirs.txt","r") as wordlist:
	for line in wordlist:
		word = line.strip() 
		test_url = target_url + "/" + word
		response = request(test_url)
		if response:
			print("[+] Subdomain URL --> " + test_url)