import segno
from segno import helpers
import pdb

#Text
def simpleText(name,text):
    generateQrCode=segno.make(text)
    generateQrCode.save(name,scale=10)
    print("QR Code généré avec succès")

#wifi
def wifi(fileName,ssid,password=None,security=None,hidden=False):
    generateWifi=segno.helpers.make_wifi(ssid,password=None,security=None,hidden=False)
    generateWifi.save(fileName,scale=10)
    print("QR Code de connexion généré avec succès")

#Coordinates
def coordinates(fileName,latitude,longitude):
    geoCoordinates=segno.helpers.make_geo(latitude,longitude)
    geoCoordinates.save(fileName,scale=10)
    print("QR Code de localisation généré avec succès")

def generateVCard(fileName,name,displayname,email,phone,url,pobox):
    vcard = segno.helpers.make_vcard(name=name,displayname=displayname,email=email,phone=phone,url=url,pobox=pobox)
    vcard.save(fileName,scale=10)
    
#Email
def email(fileName,to,cc=None,bcc=None,subject=None,body=None):
    generateEmail=segno.helpers.make_email(to,cc,bcc,subject,body)
    generateEmail.save(fileName,scale=10)
    print("Votre Email QR Code est généré avec succès")