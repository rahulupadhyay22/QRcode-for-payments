# 🎉 UPI QR Code Generator 🎉

Welcome to the **UPI QR Code Generator**! This Python application allows you to effortlessly create UPI QR codes for popular payment apps like **PhonePe**, **Google Pay**, and **Paytm** through a user-friendly graphical interface. 🚀💳

## 📦 Features

- **User-Friendly GUI:** Easily enter your UPI ID and choose your preferred payment app.
- **Multiple Payment Options:** Generate QR codes for PhonePe, Google Pay, and Paytm.
- **Image Saving Option:** Save your QR code as a `.png` image for future use. 📸

## 🚀 Getting Started

### Prerequisites

Make sure you have the following Python packages installed:

```bash
pip install qrcode[pil] pillow
```

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/upi-qr-code-generator.git
   cd upi-qr-code-generator
   ```

2. **Run the application:**

   ```bash
   python main.py
   ```

### 🎨 User Interface

Once the application is running, you'll see a beautiful interface that looks like this:

```
|-----------------------------------|
|  📝 Enter UPI ID:                |
|  [ User's UPI ID Entry Field ]    |
|                                   |
|  💳 Select Payment App:           |
|  [ Dropdown: PhonePe/GooglePay/   |
|     Paytm ]                       |
|                                   |
|  [ ] Save QR Code as Image        |
|                                   |
|      [ Generate QR Code Button ]  |
|                                   |
|  [ QR Code Image Display ]        |
|-----------------------------------|
```

### 📷 Example Usage

1. **Input your UPI ID.**
2. **Select a payment app** from the dropdown menu.
3. **Check the box** to save the QR code as an image if desired.
4. **Click the "Generate QR Code" button** to create your QR code!

Your generated QR code will appear right in the app! If you selected the save option, it will also be saved as a `.png` file in your working directory. 

## 🔧 Code Overview

The heart of the application is the `generate_qr()` function, which:
- Collects your UPI ID and selected payment app.
- Constructs a unique UPI QR code URL based on your selection.
- Displays the generated QR code in the GUI and saves it as an image if requested.

## 🎉 Screenshot

![UPI QR Code Generator Interface](path/to/your/screenshot.png)

*(Replace the path with an actual screenshot of your application)*

## 📝 License

This project is open-source and available under the [MIT License](LICENSE). Feel free to modify and share!

## 🙌 Contributing

We welcome contributions! If you'd like to enhance this project, please fork the repository and submit a pull request.

## 💬 Feedback

Have questions or suggestions? Open an issue on the GitHub repository, and we’ll get back to you!

---
