# Import the necessary modules
import qrcode
from PIL import Image

# Prompt the user for the type of QR code
print("Choose the type of QR code you want to create:")
print("1. URL")
print("2. WiFi")
print("3. vCard")
choice = int(input("Enter the number corresponding to your choice: "))

# Function to create and display the QR code
def create_and_display_qr(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    img.show()
    
    print("QR code displayed on the screen. Close the window to exit.")

# Handle different QR code types
if choice == 1:
    # Create a URL QR code
    url = input("Enter the URL you want to encode: ")
    create_and_display_qr(url)
elif choice == 2:
    # Create a WiFi QR code
    ssid = input("Enter the SSID (WiFi Name): ")
    password = input("Enter the WiFi password: ")
    security = input("Enter the security type (WPA, WEP, etc.): ")
    wifi_data = f"WIFI:T:{security};S:{ssid};P:{password};;"
    create_and_display_qr(wifi_data)
elif choice == 3:
    # Create a vCard QR code
    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email address: ")
    vcard_data = f"BEGIN:VCARD\nVERSION:3.0\nFN:{name}\nTEL:{phone}\nEMAIL:{email}\nEND:VCARD"
    create_and_display_qr(vcard_data)
else:
    print("Invalid choice. Please select a valid option (1, 2, or 3).")
