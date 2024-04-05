import qrcode
import image
qr = qrcode.QRCode(
    version = 15, 
    box_size  = 10,
    border = 5
)
data = "https://www.canva.com/design/DAFmiJzRPHw/l9J7eFxBn8x_xQ29tXm2Mg/view?utm_content=DAFmiJzRPHw&utm_campaign=designshare&utm_medium=link&utm_source=editor"
qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill="black",back_color ="white")
img.save("test.png")