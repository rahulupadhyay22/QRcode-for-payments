import qrcode


#taking upi id as input
upi_id = input("Enter UPI ID: ")

#upi://pay?pa=upi_id&pn=Name&tid=TransactionID&am=Amount&cu=Currency&tn=message

#defining the payment url based on upi id and the payment app
#you can modify the url based on the payment app you are using
phonepe_url = f"upi://pay?pa={upi_id}&pn=recepient%20Name&mc=1234"
googlepay_url = f"upi://pay?pa={upi_id}&pn=recepient%20Name&mc=1234"
paytm_url = f"upi://pay?pa={upi_id}&pn=recepient%20Name&mc=1234"

# Ask for the payment app
payment_app = input("Enter the payment app (phonepe/googlepay/paytm): ").lower()

# Generate QR code based on the selected payment app
if payment_app == "phonepe":
    qr = qrcode.make(phonepe_url)
elif payment_app == "googlepay":
    qr = qrcode.make(googlepay_url)
elif payment_app == "paytm":
    qr = qrcode.make(paytm_url)
else:
    print("Invalid payment app selected")
    qr = None

if qr:
    # Ask to save the QR code as image or not
    save_qr = input("Do you want to save the QR code as image? (y/n): ").lower()
    if save_qr == 'y':
        qr.save(f"{payment_app}_qr.png")
    # Display the QR code
    qr.show()

# Run the script and enter the UPI ID and payment app to generate the QR code. You can save the QR code as an image if you want.