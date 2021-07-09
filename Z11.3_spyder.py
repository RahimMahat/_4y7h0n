#!/usr/bin/env python

import requests, re
import urlparse  # to get the proper url



target_url = "http://localhost/mutillidae"
target_links = []


def extract_links_from(url):
	response = requests.get(target_url)
	return re.findall('(?:href=")(.*?)"', response.content)  # looking for the links on the website
	#  ?: represent no capturing part in first group and in second grouo ? is used to say non greedy
	#  it'll return the list of extracted links from the webpage


href_links = extract_links_from(target_url)
# print(href_links) 

for link in href_links:
	link = urlparse.urljoin(target_url, link)  # to join the relative url's with the base url
	# print(link)  # to get all the links present in the webpage

	if "#" in link:  # filtering the html id elements to get more accuracy in uniqueness
		link = link.split("#")[0]

	if target_url in link and link not in target_links:  # to filter only links which are associate with the target webpage 2nd condition is to get unique links
		target_links.append(link)
		print(link)
