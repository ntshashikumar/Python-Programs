import qrcode

print("QR Code Generator ")
print("Created by @Shashi")

# data="www.youtube.com/@shashikumarnt"
data=input("Enter code to create to an QR Code >>")
qr=qrcode.make(data)
qr.save("C:/Users/Admin/Desktop/QRCode.png")
print("QR Code generated Sucessfully")
