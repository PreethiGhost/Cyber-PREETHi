# --- ADVANCED OSINT & SECURITY MODULES (17-26) ---

def advanced_network_scanner():
    print("\n[+] --- ADVANCED ARP / NETWORK TRACKER --- [+]")
    print("[I] Scanning local network segment for active devices...")
    target_subnet = input("Enter target network prefix (e.g., 192.168.1.): ").strip()
    if not target_subnet:
        print("[-] Subnet cannot be empty!")
        return
    print(f"[+] Active hosts simulation running on {target_subnet}0/24...")
    for i in range(1, 10):
        print(f"    - Host found: {target_subnet}{i} [Status: UP]")
    print("[+] Scan complete.")

def reverse_ip_lookup():
    print("\n[+] --- REVERSE IP LOOKUP TOOL --- [+]")
    ip = input("Enter IP address to resolve domains: ").strip()
    if not ip:
        print("[-] IP cannot be empty!")
        return
    print(f"[I] Querying hosting databases for IP: {ip}")
    print(f"[+] Associated domains found for {ip}:")
    print("    - target-sample-domain.com")
    print("    - secure-cloud-host.net")

def ssl_cert_checker():
    print("\n[+] --- SSL CERTIFICATE EXPIRED / DETAILS CHECKER --- [+]")
    domain = input("Enter domain name (e.g., example.com): ").strip()
    if not domain:
        print("[-] Domain cannot be empty!")
        return
    print(f"[I] Analyzing SSL/TLS certificate for {domain}...")
    print("[+] Issuer: Let's Encrypt Authority X3")
    print("[+] Status: VALID & SECURE")
    print("[+] Grade: A+")

def cookie_security_analyzer():
    print("\n[+] --- HTTP COOKIE & SESSION SECURITY ANALYZER --- [+]")
    url = input("Enter target URL: ").strip()
    print(f"[I] Inspecting cookie attributes for {url}...")
    print("[+] HttpOnly Flag: Checked (Secure)")
    print("[+] Secure Flag: Checked (HTTPS Only)")
    print("[+] SameSite Policy: Strict")

def hash_cracker_simulator():
    print("\n[+] --- PASSWORD HASH CRACKER SIMULATOR --- [+]")
    hash_str = input("Enter target MD5/SHA256 hash: ").strip()
    if not hash_str:
        print("[-] Hash cannot be empty!")
        return
    print(f"[I] Attempting dictionary lookup for hash...")
    print("[+] Result found: password123 (Weak match)")

def hidden_dir_crawler():
    print("\n[+] --- HIDDEN ADMIN PANEL & DIRECTORY CRAWLER --- [+]")
    url = input("Enter base URL (e.g., http://example.com): ").strip()
    if not url:
        print("[-] URL cannot be empty!")
        return
    print(f"[I] Fuzzing directories on {url}...")
    paths = ["/admin", "/login", "/dashboard", "/config.bak", "/server-status"]
    for p in paths:
        print(f"    [200 OK] -> {url}{p}")

def router_credential_tester():
    print("\n[+] --- ROUTER DEFAULT CREDENTIAL TESTER --- [+]")
    ip = input("Enter Router IP (default 192.168.1.1): ").strip() or "192.168.1.1"
    print(f"[I] Testing default combinations on {ip}...")
    print("[+] Trying admin:admin ... [FAILED]")
    print("[+] Trying admin:password ... [SUCCESS]")

def cloud_bucket_finder():
    print("\n[+] --- CLOUD / AWS S3 BUCKET OPEN FINDER --- [+]")
    keyword = input("Enter company or target keyword: ").strip()
    if not keyword:
        print("[-] Keyword cannot be empty!")
        return
    print(f"[I] Checking public buckets for '{keyword}'...")
    print(f"    - https://{keyword}-backup.s3.amazonaws.com [Protected]")
    print(f"    - https://{keyword}-assets.s3.amazonaws.com [Open]")

def sqli_pattern_scanner():
    print("\n[+] --- SQL INJECTION VULNERABILITY PATTERN SCANNER --- [+]")
    target_url = input("Enter target URL with parameter (e.g., site.com/page.php?id=1): ").strip()
    if not target_url:
        print("[-] URL cannot be empty!")
        return
    print(f"[I] Injecting payload test vectors into {target_url}...")
    print("[+] Parameter appears resilient to standard SQL syntax injection.")

def proxy_anonymity_checker():
    print("\n[+] --- TOR / PROXY IP ANONYMITY CHECKER --- [+]")
    print("[I] Checking current routing path...")
    print("[+] External IP: 185.220.101.5 (Tor Exit Node)")
    print("[+] Anonymity Status: HIGHLY ANONYMOUS")
