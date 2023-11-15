import eel
import segno
import db
import uuid

@eel.expose
def createQR():
    uid = str(uuid.uuid4())
    qrcode = segno.make_qr(uid)
    qrcode.save(uid + ".png", scale=10)
    print(uid)
    db.saveQR(uid)
    return uid
