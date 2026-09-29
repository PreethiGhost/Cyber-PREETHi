import time
import sys

print("Initializing system bypass...\n")
time.sleep(1)

# ಫೇಕ್ ಹ್ಯಾಕಿಂಗ್ ಅಥವಾ ಇನ್ಸ್ಟಾಲೇಷನ್ ಸ್ಟೆಪ್ಸ್
messages = [
    "Connecting to target device...",
    "Bypassing firewall security...",
    "Accessing personal gallery and messages...",
    "Downloading sensitive data (10%)...",
    "Downloading sensitive data (50% nilaiyithu)...",
    "Downloading sensitive data (100% complete!).",
    "Formatting internal storage in 3... 2... 1...",
    "Just Kidding! 😄 Happy Prank!"
]

for msg in messages:
    for char in msg:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    print()
    time.sleep(0.5)
