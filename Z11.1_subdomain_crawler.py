#!/usr/bin/env python

import requests


def request(url):
	try:
		return requests.get("http://" +url)
	except requests.exceptions.ConnectionError:
		pass

target_url = "google.com"
with open("small-subdomain-wodlist.txt","r") as wordlist:
	for line in wordlist:
		word = line.strip()  # to strip the new line character in the wordlist
		test_url = word + "." + target_url  # eg. mail.google.com
		response = request(test_url)
		if response:
			print("[+] Subdomain discovered --> " + test_url)