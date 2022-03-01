import qrcode
'''
qr = qrcode.QRCode(
    version = 3,
    box_size= 3,
    border=5
)

qr.add_data = "http://www.facebook.com" #/groups/932755930759627"

img = qr.make_image(fill_color = "black", back_color = "white")

'''
img = qrcode.make("https://www.facebook.com/groups/932755930759627")


img.save("qrhubfb.png")