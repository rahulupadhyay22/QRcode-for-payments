#MAKE A GUI OF THIS ABOVE CODE
import qrcode
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image


def generate_qr():
    upi_id = upi_id_entry.get()
    payment_app = payment_app_var.get().lower()

    if not upi_id:
        messagebox.showerror("Error", "Please enter UPI ID")
        return

    phonepe_url = f"upi://pay?pa={upi_id}&pn=recepient%20Name&mc=1234"
    googlepay_url = f"upi://pay?pa={upi_id}&pn=recepient%20Name&mc=1234"
    paytm_url = f"upi://pay?pa={upi_id}&pn=recepient%20Name&mc=1234"

    if payment_app == "phonepe":
        qr = qrcode.make(phonepe_url)
    elif payment_app == "googlepay":
        qr = qrcode.make(googlepay_url)
    elif payment_app == "paytm":
        qr = qrcode.make(paytm_url)
    else:
        messagebox.showerror("Error", "Invalid payment app selected")
        return

    qr_image = qr.get_image()
    qr_image = qr_image.resize((200, 200), Image.LANCZOS)
    qr_photo = ImageTk.PhotoImage(qr_image)

    qr_label.config(image=qr_photo)
    qr_label.image = qr_photo

    if save_var.get():
        qr.save(f"{payment_app}_qr.png")

app = tk.Tk()
app.title("UPI QR Code Generator")

tk.Label(app, text="Enter UPI ID:").grid(row=0, column=0, padx=10, pady=10)
upi_id_entry = tk.Entry(app)
upi_id_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(app, text="Select Payment App:").grid(row=1, column=0, padx=10, pady=10)
payment_app_var = tk.StringVar(value="phonepe")
tk.OptionMenu(app, payment_app_var, "phonepe", "googlepay", "paytm").grid(row=1, column=1, padx=10, pady=10)

save_var = tk.BooleanVar()
tk.Checkbutton(app, text="Save QR Code as Image", variable=save_var).grid(row=2, columnspan=2, padx=10, pady=10)

tk.Button(app, text="Generate QR Code", command=generate_qr).grid(row=3, columnspan=2, padx=10, pady=10)

qr_label = tk.Label(app)
qr_label.grid(row=4, columnspan=2, padx=10, pady=10)

app.mainloop()

# Run the script and enter the UPI ID and payment app to generate the QR code. You can save the QR code as an image if you want.
