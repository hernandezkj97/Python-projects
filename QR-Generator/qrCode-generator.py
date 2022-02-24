import qrcode
import image
qr=qrcode.QRCode(
    version=15,
    box_size=10,
    border=5
)

data = "https://www.youtube.com/watch?v=dQw4w9WgXcQ" 
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill_color="black", back_color="white")
img.save("qr.png")