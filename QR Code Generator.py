import qrcode

def generate_qr_code(data, file_name="qrcode.png"):
    """Generate a QR code from the provided data and save it as an image."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_name)
    print(f"QR code saved as {file_name}")

def main():
    print("QR Code Generator")
    data = input("Enter the data to encode (e.g., URL, text): ").strip()
    file_name = input("Enter the file name to save as (default: qrcode.png): ").strip() or "qrcode.png"
    generate_qr_code(data, file_name)

if __name__ == "__main__":
    main()
