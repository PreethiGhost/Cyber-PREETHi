from scapy.all import ARP, Ether, srp

print("--- Simple Network Scanner ---")

# ನಿಮ್ಮ ಲೋಕಲ್ ನೆಟ್‌ವರ್ಕ್ ಐಪಿ ಅಡ್ರೆಸ್ ರೇಂಜ್ (ಉದಾಹರಣೆಗೆ 192.168.1.1/24)
target_ip = input("Enter IP range to scan (e.g., 192.168.1.1/24): ")

# ARP ಪ್ಯಾಕೆಟ್ ಸೃಷ್ಟಿಸುವುದು
arp = ARP(pdst=target_ip)
ether = Ether(dst="ff:ff:ff:ff:ff:ff")
packet = ether/arp

print("Scanning network, please wait...")
result = srp(packet, timeout=3, verbose=0)[0]

devices = []
for sent, received in result:
    devices.append({'ip': received.psrc, 'mac': received.hwsrc})

print("\nAvailable devices in the network:")
print("IP Address          MAC Address")
print("-" * 40)
for device in devices:
    print(f"{device['ip']:17}   {device['mac']}")

