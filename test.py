import pywhatkit as kit
import time

print("Automation script configured...")
phone_number = "+918310873590"
message = "Hello! Termux Automation success aagide."

kit.sendwhatmsg_instantly(phone_number, message, wait_time=10)
print("Process finished!")

