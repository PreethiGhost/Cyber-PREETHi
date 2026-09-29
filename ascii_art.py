import pyfiglet

print("--- ASCII Art Text Generator ---")

# ನೀವು ಡಿಸೈನ್ ಮಾಡಬೇಕಾದ ಹೆಸರನ್ನು ಇಲ್ಲಿ ಕೇಳುತ್ತದೆ
text = input("Enter text to convert into ASCII art: ")

# ASCII ಆರ್ಟ್ ಸೃಷ್ಟಿಸಿ ಪ್ರಿಂಟ್ ಮಾಡುವುದು
ascii_banner = pyfiglet.figlet_format(text)

print("\nHere is your ASCII Art:")
print(ascii_banner)
