import subprocess
import optparse
import re


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
    # print('[+] Changed your ' + interface + ' to new mac ' + mac_addr)

def get_mac(interface):
    ifconf_result = subprocess.check_output(["ifconfig", interface])
    mac_addr_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconf_result)
    if mac_addr_search_result:
        return mac_addr_search_result.group(0)
    else:
        print("[-] Couldn't find MAC Address for your "+interface+" interface")

options = get_argumets()
current_mac = get_mac(options.interface)
print("Current MAC Address is: "+str(current_mac))

mac_changer(options.interface, options.new_mac)
current_mac = get_mac(options.interface)
if current_mac == options.new_mac:
    print("[+] MAC Address was successfully changed to " + current_mac)
else:
    print("[-] MAC Address did not changed")

