import socket
import sys
from datetime import datetime
import threading
from queue import Queue
import urllib.request
import json
import time

# ANSI Color Codes for Styling
R = '\033[91m' # Red
G = '\033[92m' # Green
Y = '\033[93m' # Yellow
B = '\033[94m' # Blue
M = '\033[95m' # Magenta
C = '\033[96m' # Cyan
W = '\033[97m' # White
RES = '\033[0m' # Reset Color

def clear_screen():
    print("\033c", end="")

# Stylish GHOSor Banner
def show_banner():
    clear_screen()
    print(f"{M}=" * 60)
    print(f"{C}  ██████╗ ██╗  ██╗ ██████╗ ███████╗ ██████╗ ██████╗ ")
    print(f"{C} ██╔════╝ ██║  ██║██╔═══██╗██╔════╝██╔═══██╗██╔══██╗")
    print(f"{C} ██║  ███╗███████║██║   ██║███████╗██║   ██║██████╔╝")
    print(f"{C} ██║   ██║██╔══██║██║   ██║╚════██║██║   ██║██╔══██╗")
    print(f"{C} ╚██████╔╝██║  ██║╚██████╔╝███████║╚██████╔╝██║  ██║")
    print(f"{C}  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═╝")
    print(f"{Y}          [ ADVANCED NETWORK RESEARCH TOOL ]          ")
    print(f"{M}=" * 60)
    print(f"{W}  Coder / Owner : {G}GHOSor (Preethu)")
    print(f"{M}=" * 60 + f"{RES}\n")

show_banner()

# Menu Options
print(f"{Y}[1]{W} IP Geolocation Lookup")
print(f"{Y}[2]{W} Multi-Threaded Port Scanner (1-1024)")
print(f"{Y}[3]{W} Run Both (Location + Port Scan)")
print(f"{Y}[4]{W} Exit Tool\n")

choice = input(f"{C}Enter your choice (1-4): {RES}")

if choice == '1':
    target_host = input(f"{Y}[+] Enter Target IP or Hostname: {RES}")
    try:
        target_ip = socket.gethostbyname(target_host)
    except socket.gaierror:
        print(f"{R}[!] Hostname could not be resolved.{RES}")
        sys.exit()
    
    print(f"\n{G}[*] Fetching Location for: {target_ip}{RES}")
    try:
        url = f"http://ip-api.com/json/{target_ip}"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=3) as response:
            data = json.loads(response.read().decode())
            if data['status'] == 'success':
                print(f"\n{M}--- IP GEOLOCATION INFO ---{RES}")
                print(f"{W}Country  : {G}{data.get('country', 'N/A')}{RES}")
                print(f"{W}Region   : {G}{data.get('regionName', 'N/A')}{RES}")
                print(f"{W}City     : {G}{data.get('city', 'N/A')}{RES}")
                print(f"{W}ISP      : {G}{data.get('isp', 'N/A')}{RES}")
                print(f"{M}---------------------------\n{RES}")
            else:
                print(f"\n{R}[!] Geolocation info could not be fetched.{RES}")
    except:
        print(f"\n{R}[!] Network error during geolocation check.{RES}")

elif choice == '2' or choice == '3':
    target_host = input(f"{Y}[+] Enter Target IP or Hostname: {RES}")
    try:
        target_ip = socket.gethostbyname(target_host)
    except socket.gaierror:
        print(f"{R}[!] Hostname could not be resolved.{RES}")
        sys.exit()

    if choice == '3':
        print(f"\n{G}[*] Fetching Location First...{RES}")
        try:
            url = f"http://ip-api.com/json/{target_ip}"
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=3) as response:
                data = json.loads(response.read().decode())
                if data['status'] == 'success':
                    print(f"\n{M}--- IP GEOLOCATION INFO ---{RES}")
                    print(f"{W}Country  : {G}{data.get('country', 'N/A')}{RES}")
                    print(f"{W}Region   : {G}{data.get('regionName', 'N/A')}{RES}")
                    print(f"{W}City     : {G}{data.get('city', 'N/A')}{RES}")
                    print(f"{W}ISP      : {G}{data.get('isp', 'N/A')}{RES}")
                    print(f"{M}---------------------------\n{RES}")
        except:
            pass

    print(f"\n{G}[*] Starting Port Scan on {target_ip} (1 to 1024)... Please wait.{RES}\n")
    print(f"{M}=" * 50 + f"{RES}")

    print_lock = threading.Lock()
    q = Queue()

    def port_scan(port):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            result = s.connect_ex((target_ip, port))
            if result == 0:
                with print_lock:
                    print(f"{W}Port {port}: {G}OPEN ✅{RES}")
            s.close()
        except:
            pass

    def threader():
        while True:
            worker = q.get()
            port_scan(worker)
            q.task_done()

    for x in range(1, 1025):
        q.put(x)

    for x in range(100):
        t = threading.Thread(target=threader)
        t.daemon = True
        t.start()

    q.join()

    print(f"{M}=" * 50 + f"{RES}")
    print(f"{C} Scanning Complete! GHOSor Tool Finished Successfully.{RES}")
    print(f"{M}=" * 50 + f"{RES}")

elif choice == '4':
    print(f"\n{R}[!] Exiting GHOSor Tool. Goodbye Preethu!{RES}")
    sys.exit()

else:
    print(f"\n{R}[!] Invalid Choice! Please run the tool again and select 1-4.{RES}")
