import segno
from qrcode import myqrcode

"""
price_tag = segno.make("Hello World")
#scale=dimensions
price_tag.save("hello-world.png",dark='darkred',light='lightblue',scale=10)
"""
myQrCode=myqrcode.simpleText("mySauvegardes.png","Hi getting QR Code with python")
#myQrCode.save()