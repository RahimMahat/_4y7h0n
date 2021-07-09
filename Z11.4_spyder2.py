#!/usr/bin/env python

import requests, re
import urlparse

#  improvise version of the last spyder in which we'll discover all the links from not only the 
#  single target webpage but alos from the entire website

target_url = "http://localhost/mutillidae/"
target_links = []

def extract_links_from(url):
	response = requests.get(target_url)
	return re.findall('(?:href=")(.*?)"', response.content)

def crawl(url):
	href_links = extract_links_from(url)

	for link in href_links:
		link = urlparse.urljoin(url, link)

		if "#" in link:
			link = link.split("#")[0]

		if url in link and link not in target_links:
			target_links.append(link)
			print(link)
			crawl(link)  # recursing over the subdomains we got

crawl(target_url)