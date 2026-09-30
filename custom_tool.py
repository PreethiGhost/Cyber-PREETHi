# --- MAIN MENU DISPLAY & EXECUTION LOOP ---
def main_menu():
    while True:
        print("\n========================================")
        print("         Cyber-PREETHi TOOL             ")
        print("========================================")
        print("[1-16] Previous Core Security Modules")
        print("[17] Advanced ARP / Network Scanner")
        print("[18] Reverse IP Lookup Tool")
        print("[19] SSL Certificate Checker")
        print("[20] HTTP Cookie Security Analyzer")
        print("[21] Password Hash Cracker Simulator")
        print("[22] Hidden Admin Panel Crawler")
        print("[23] Router Credential Tester")
        print("[24] Cloud / AWS S3 Bucket Finder")
        print("[25] SQL Injection Pattern Scanner")
        print("[26] Tor / Proxy Anonymity Checker")
        print("[00] Exit")
        
        choice = input("\nEnter your choice Preetu: ").strip()
        
        if choice == '17':
            advanced_network_scanner()
        elif choice == '18':
            reverse_ip_lookup()
        elif choice == '19':
            ssl_cert_checker()
        elif choice == '20':
            cookie_security_analyzer()
        elif choice == '21':
            hash_cracker_simulator()
        elif choice == '22':
            hidden_dir_crawler()
        elif choice == '23':
            router_credential_tester()
        elif choice == '24':
            cloud_bucket_finder()
        elif choice == '25':
            sqli_pattern_scanner()
        elif choice == '26':
            proxy_anonymity_checker()
        elif choice == '00':
            print("[+] Exiting Cyber-PREETHi. Stay safe, Preetu!")
            break
        else:
            print("[-] Invalid choice or core module selected. Try again!")

if __name__ == "__main__":
    main_menu()

