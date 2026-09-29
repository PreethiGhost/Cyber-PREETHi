import time
import os
import random
import subprocess

def get_system_stats():
    try:
        # Battery status
        b_output = subprocess.check_output(['termux-battery-status']).decode('utf-8')
        import json
        b_data = json.loads(b_output)
        battery = int(b_data.get('percentage', 85))
    except:
        battery = 90
    return battery

try:
    while True:
        os.system('clear')
        
        # 1. Top Dangerous Border
        print("\033[91m═════════════════════════════════════════════════════════════════\033[0m")
        print("\033[95m [!] CLASSIFIED MAINFRAME // ROOT BYPASS ACTIVE [!] \033[0m")
        print("\033[91m═════════════════════════════════════════════════════════════════\033[0m")
        
        # 2. DODDA NAME: GHOST
        print("\033[92m  ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗\033[0m")
        print("\033[93m ██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝\033[0m")
        print("\033[91m ██║  ███╗███████║██║   ██║███████╗   ██║   \033[0m")
        print("\033[96m ██║   ██║██╔══██║██║   ██║╚════██║   ██║   \033[0m")
        print("\033[95m ╚██████╔╝██║  ██║╚██████╔╝███████║   ██║   \033[0m")
        print("\033[91m═════════════════════════════════════════════════════════════════\033[0m")
        
        # 3. Live Server Status, RAM & Storage
        current_time = time.strftime("%H:%M:%S")
        battery = get_system_stats()
        
        print(f" \033[96m[SERVER]:\033[92m ONLINE \033[0m | \033[96m[IP]:\033[93m 192.168.43.99 \033[0m | \033[96m[TIME]:\033[92m {current_time}")
        print(f" \033[96m[RAM USAGE]:\033[93m 3.5GB / 8.0GB (43%)\033[0m   | \033[96m[STORAGE]:\033[91m 112GB / 128GB\033[0m")
        print(f" \033[96m[BATTERY]:\033[92m {battery}% \033[0m           | \033[96m[TARGET]:\033[91m READY FOR LAUNCH\033[0m")
        print("\033[91m─────────────────────────────────────────────────────────────────\033[0m")
        
        # 4. Dangerous Hacker Logs & Options
        print(" \033[95m[ACTIVE DEEP-WEB THREAT MODULES]:\033[0m")
        
        threats = [
            ("\033[91m[CRITICAL]", "Injecting payload into core system partitions..."),
            ("\033[93m[WARNING] ", "Firewall breached! External backdoor open on port 4444."),
            ("\033[92m[SUCCESS] ", "Biometric encryption bypassed successfully."),
            ("\033[96m[SECURE]  ", "Routing traffic through 7 proxy layers (Darknet active)."),
            ("\033[95m[ALERT]   ", "Overwriting kernel memory sectors... TARGET LOCKED.")
        ]
        
        # Select 4 random warning lines to display nicely
        selected_threats = random.sample(threats, 4)
        for t_tag, t_msg in selected_threats:
            code = random.randint(10000, 99999)
            print(f" {t_tag} (0x{code}) -> {t_msg}")
            
        print("\033[91m─────────────────────────────────────────────────────────────────\033[0m")
        print(" \033[92m[STATUS]: SYSTEM FULLY COMPROMISED. (Press Ctrl + C to exit)\033[0m")
        
        # Smooth delay so it doesn't flicker aggressively
        time.sleep(1.2)

except KeyboardInterrupt:
    print("\n\n\033[92m[+] Terminated safely. Welcome back, Preethu!\033[0m")
