import socket
import sys
from datetime import datetime

print("--- Simple Port Scanner ---")

# ಟಾರ್ಗೆಟ್ ಹೋಸ್ಟ್ ಅಥವಾ ಐಪಿ ಅಡ್ರೆಸ್ ಕೇಳುವುದು
target_host = input("Enter target IP or website to scan: ")

print("-" * 50)
print(f"Scanning target: {target_host}")
print(f"Time started: {str(datetime.now())}")
print("-" * 50)

try:
    # ಸಾಮಾನ್ಯ ಮತ್ತು ಪ್ರಮುಖ ಪೋರ್ಟ್‌ಗಳನ್ನು ಸ್ಕ್ಯಾನ್ ಮಾಡುವುದು
    ports = [21, 22, 23, 80, 443, 3306, 8080]

    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target_host, port))

        if result == 0:
            print(f"Port {port}: OPEN")
        else:
            print(f"Port {port}: CLOSED")
        s.close()

except KeyboardInterrupt:
    print("\nExiting script.")
    sys.exit()
except socket.gaierror:
    print("\nHostname could not be resolved.")
    sys.exit()
except socket.error:
    print("\nCould not connect to server.")
    sys.exit()
