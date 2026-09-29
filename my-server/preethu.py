import time
from plyer import notification

print("Remind madtidde...")
time.sleep(2)

notification.notify(
    title="Preethu Alert!",
    message="Svalpa break tegesi!",
    app_name='Reminder',
    timeout=5
)
print("Done!")
import time
from plyer import notification

def set_reminder():
    print("--- ರಿಮೈಂಡರ್ ಸ್ಟಾರ್ಟ್ ಆಗಿದೆ ---")
    
    title = "ಪ್ರೀತು!"
    message = "ಸ್ವಲ್ಪ ನೀರು ಕುಡಿ!"
    
    time.sleep(3)
    
    notification.notify(
        title=title,
        message=message,
        app_name='Smart Reminder',
        timeout=10
    )
    print("ರಿಮೈಂಡರ್ ಸೆಂಡ್ ಆಗಿದೆ!")

if __name__ == "__main__":
    set_reminder()
