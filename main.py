import eel
import segno
import db
import uuid
import json
from os import path
import datetime

eel.init('web')

@eel.expose
def createQR():
    uid = str(uuid.uuid4())
    qrcode = segno.make_qr(uid)
    qrcode.save("C:\\Users\\edwar\\PycharmProjects\\ProiectPython\\web\\" + uid + ".png", scale=10)
    db.saveQR(uid)
    return uid


@eel.expose
def saveQR(st):
    filename = 'database.json'
    listObj = getQRs()

    listObj.append({
        "id": st,
        "taken": 0,
        "created": str(datetime.datetime.now())
    })

    with open(filename, 'w') as json_file:
        json.dump(listObj, json_file,
                  indent=4,
                  separators=(',', ': '))

@eel.expose
def getQRs():
    filename = 'database.json'
    listObj = []
    listId = []

    if path.isfile(filename) is False:
        raise Exception("File not found")

    with open(filename) as fp:
        listObj = json.load(fp)

    return listObj

@eel.expose
def getIDs():

    listId = []

    for x in getQRs():
        listId.append(x['id'])
        print(x['id'])


    return listId

@eel.expose
def getQRNumbers():
    return len(getQRs())

@eel.expose
def check(str):
    for item in getQRs():
        if str == item["id"]:
            return 1

    return 0

@eel.expose
def open_scanner():
    import qr_reader

eel.start('index.html', mode='chrome', port=8080, cmdline_args=['--start-maximized'])
