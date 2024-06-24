import qrcode
import qrcode.constants

qr= qrcode.QRCode(version=1,
                  error_correction=qrcode.constants.ERROR_CORRECT_H,
                  box_size=20,
                  border=2)
qr.add_data("https://www.youtube.com/channel/UCAHqow44WJNCeUdszxAAVlw")
qr.make(fit=True)

img = qr.make_image(fill_color="#FF0000",back_color="black")
img.save("AP.png")