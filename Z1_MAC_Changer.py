#!/usr/bin/env python

import subprocess  # to run the systme commands
import optparse  # to take the command line arguments from user


# i) CLI :
def get_argumets():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change it's MAC_Address")
    parser.add_option("-m", "--mac", dest="new_mac", help="Your new MAC Address")
    (options, argumets) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify the interface, use --help for help")
    elif not options.new_mac:
        parser.error("[-] Please specify the new MAC address, use --help for help")
    return options


def mac_changer(interface, mac_addr):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac_addr])
    subprocess.call(["ifconfig", interface, "up"])
    print('[+] Changed your ' + interface + ' to new mac ' + mac_addr)


options = get_argumets()
mac_changer(options.interface, options.new_mac)

'''
# ii) simple script:

interface = input("[+] Choose your interface to change the MAC address: ")
subprocess.call(f"ifconfig {interface} down", shell=True)
print(f"[+] Your interface {interface} is down now")

mac_addr = input("[+] Input the MAC address you want to set in the format [00:11:22:33:44:55] : ")
subprocess.call(f"ifconfig eth0 hw ether {mac_addr}", shell=True)
print(f"[+] Your MAC address is changed to {mac_addr}")

print(f"[+] Setting your {interface} up")
subprocess.call(f"ifconfig {interface} up", shell=True)
print("[+] Done")

'''
