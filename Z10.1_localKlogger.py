#!/usr/bin/env python

import pynput.keyboard  # we're only listening for keyboard input pynput also allow us mouse interaction

def process_key_press(key):
	print(key)



keyboard_listener = pynput.keyboard.Listener(on_press=process_key_press)  # we are creating a listener object
# and with 'on_press' we define a call back function

with keyboard_listener:  
	keyboard_listener.join()  # starting the listener