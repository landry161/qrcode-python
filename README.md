# qrcode-python
# How to use this project

#First install segno
#pip install segno

"""

#Text
myQrCode=myqrcode.simpleText("mySauvegardes.png","Hi getting QR Code with python")

#Email
myQrCode=myqrcode.email("myEmail.png","myemail@yahoo.fr","","","Hi","How are you guy, nice to meet you. Can you use this project and share it? Thanks")

#Geolocation
myQrCode=myqrcode.coordinates("geoCoordinates.png",1.21124,-3.214545)

#Wifi
myQrCode=myqrcode.wifi("wifi.png","Bbox-FXXXXXX","password","WEP",False)

#VCARD
myQrCode=myqrcode.generateVCard("finalVCARD.png",name="Gary Fletcher",displayname="Gary Fletcher",email="gary@fakemail.com",phone="+330111111011",url="https://www.myfakewebsite.com",pobox="123 Main St, Anytown USA")

"""