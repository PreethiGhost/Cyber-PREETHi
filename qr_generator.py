import qrcode

print("--- QR Code Generator ---")
# ನೀವು ಯಾವ ಲಿಂಕ್ ಅಥವಾ ಟೆಕ್ಸ್ಟ್ ಗಾಗಿ QR ಕೋಡ್ ಮಾಡಬೇಕೋ ಅದನ್ನು ಇಲ್ಲಿ ಕೊಡಿ
data = input("Enter text or URL to generate QR code: ")

filename = input("Enter filename to save (e.g., my_qr.png): ")

# QR ಕೋಡ್ ಸೃಷ್ಟಿಸುವುದು
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)
qr.add_data(data)
qr.make(fit=True)

# ಇಮೇಜ್ ಆಗಿ ಸೇವ್ ಮಾಡುವುದು
img = qr.make_image(fill_color="black", back_color="white")
img.save(filename)

print(f"Success! QR Code saved as {filename}")
