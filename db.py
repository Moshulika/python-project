import json
from os import path
import datetime


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


def getQRs():
    filename = 'database.json'
    listObj = []

    if path.isfile(filename) is False:
        raise Exception("File not found")

    with open(filename) as fp:
        listObj = json.load(fp)

    return listObj


def check(str):
    for item in getQRs():
        if str == item["id"]:
            return 1

    return 0
