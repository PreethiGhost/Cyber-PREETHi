import time
import sys
import random

print("Initializing emergency kernel override...\n")
time.sleep(1)

# ಡೇಂಜರಸ್ ಸಿಸ್ಟಮ್ ವಾರ್ನಿಂಗ್ ಮತ್ತು ಫೇಕ್ ಎರರ್‌ಗಳು
warnings = [
    "[!] WARNING: Root permission breached from external IP.",
    "[!] CRITICAL: CPU core temperature reaching 98°C...",
    "[!] Erasing system partitions... /dev/sda1",
    "[!] Deleting user gallery and documents...",
    "[!] Injecting backdoor payload into kernel...",
    "[!] SYSTEM CORRUPTED. Rebooting in 3 seconds..."
]

try:
    while True:
        # ಯಾದೃಚ್ಛಿಕವಾಗಿ ಡೇಂಜರಸ್ ಕೋಡ್‌ಗಳು ಮತ್ತು ಎರರ್‌ಗಳನ್ನು ಪ್ರಿಂಟ್ ಮಾಡುವುದು
        err_code = random.randint(1000, 9999)
        print(f"0x{err_code} - MEMORY_ACCESS_VIOLATION at 0x7ffd58")
        time.sleep(0.05)

        if random.randint(1, 15) == 1:
            msg = random.choice(warnings)
            print(f"\033[91m{msg}\033[00m") # ಕೆಂಪು ಬಣ್ಣದಲ್ಲಿ ಪ್ರಿಂಟ್ ಆಗುತ್ತದೆ
            time.sleep(0.4)

except KeyboardInterrupt:
    print("\n\n[+] Prank stopped! Relax, your phone is safe! 😄")
    sys.exit()
