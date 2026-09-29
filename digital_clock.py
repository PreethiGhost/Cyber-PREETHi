import time
import os

print("--- Digital Clock ---")
print("Press Ctrl+C to exit the clock.\n")

try:
    while True:
        # ಪ್ರಸ್ತುತ ಸಮಯವನ್ನು ಪಡೆಯುವುದು
        current_time = time.strftime("%H:%M:%S")
        current_date = time.strftime("%d-%m-%Y")

        # ಸ್ಕ್ರೀನ್ ಕ್ಲೀನ್ ಮಾಡಿ ಸಮಯವನ್ನು ಪ್ರದರ್ಶಿಸುವುದು
        print(f"\rDate: {current_date} | Time: {current_time}", end="")
        time.sleep(1)
except KeyboardInterrupt:
    print("\n\nClock stopped!")
