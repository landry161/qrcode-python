import segno
import pdb

def simpleText(name,text):
    generateQrCode=segno.make(text)
    generateQrCode.save(name,scale=10)
    print("QR Code généré avec succès")
