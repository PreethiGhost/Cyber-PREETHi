import random
import string

print("--- Secure Password Generator ---")
length = int(input("Enter password length (e.g., 8, 12): "))

# ಅಕ್ಷರಗಳು, ನಂಬರ್‌ಗಳು ಮತ್ತು ಸಿಂಬಲ್‌ಗಳ ಒಟ್ಟು ಕಲೆಕ್ಷನ್
characters = string.ascii_letters + string.digits + string.punctuation

# ಯಾದೃಚ್ಛಿಕವಾಗಿ ಪಾಸ್‌ವರ್ಡ್ ಸೃಷ್ಟಿಸುವುದು
password = "".join(random.choice(characters) for i in range(length))

print(f"Generated Password: {password}")

