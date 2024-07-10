import qrcode

img = qrcode.make(
    'https://www.bmw.in/en/index.html'
    )
img.save('myQRcode.png')
img.show()
