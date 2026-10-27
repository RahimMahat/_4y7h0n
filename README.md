# _4y7h0n

A collection of Python scripts written while studying network security and
ethical hacking concepts — MAC spoofing, ARP/DNS manipulation, packet
sniffing, basic web reconnaissance, and keylogging mechanics.

## Purpose

This repository exists **for educational study only**, as part of learning
how common network attacks and reconnaissance techniques work at the code
level. It documents concepts, not a toolkit to run against real targets.

## Scope and limitations

- These scripts are learning exercises, not production security tools.
  Several contain hardcoded values, incomplete error handling, or
  leftover debug code.
- Nothing here should be run against any network, host, or account you do
  not own and do not have explicit written authorization to test.
- This README intentionally does not include setup or usage instructions.

## Legal and ethical notice

Using these techniques against systems you don't own or lack permission
to test is illegal in most jurisdictions (e.g., under the U.S. Computer
Fraud and Abuse Act, the UK Computer Misuse Act, and equivalent laws
elsewhere) and can cause real harm to others. Any experimentation should
be confined to an isolated lab environment (e.g., your own VMs) that you
fully control.

## Contents (by topic)

| Area | Files |
|---|---|
| MAC address manipulation | `Z1_MAC_Changer.py`, `Z1_MAC_Changer_Algo.py` |
| Network/ARP scanning | `Z2_Net_Scanner.py`, `Z2_Net_Scanner_CLI.py` |
| ARP spoofing / detection | `Z3_ARP_Spoofer.py`, `Z3_ARP_Spoofer_Algo.py`, `Z8_ARP_Spoof_Detector.py` |
| Packet sniffing | `Z4_PacketSniffer.py` |
| DNS spoofing | `Z5_DNS_Spoofer.py` |
| Traffic/file interception | `Z6_File_Interceptor.py`, `Z7_Code_Injector.py` |
| Credential/profile recovery concepts | `Z9_DER.py`, `Z9.1_wifi_profiles.py`, `Z9.2_Download.py` |
| Keylogging concepts | `Z10.1_localKlogger.py`, `Z10.2_improvedKlogger.py`, `Z10_remoteKlogger.py` |
| Web reconnaissance | `Z11.1_subdomain_crawler.py`, `Z11.2_directories.py`, `Z11.3_spyder.py`, `Z11.4_spyder2.py` |
| Login brute-force concepts | `Z12_Guess_login.py` |

## License

No license is specified; all rights reserved by default. Do not redistribute
or reuse this code for anything other than personal study.
