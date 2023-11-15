import cv2
import db
import time
import serial
from win10toast import ToastNotifier


com = 0

try:
    arduino = serial.Serial(port='COM4', baudrate=115200, timeout=0.1)
    com = 1
except:
    print("COM4 device not connected")

def communicate(t):

    if com == 1:
        arduino.write(bytes('1', 'utf-8'))


toast = ToastNotifier()
toast.show_toast("QR Scanner has started", "Press 'Q' to exit the scanner", duration=20, icon_path="favicon.ico", threaded=True)

cap = cv2.VideoCapture(0)

detector = cv2.QRCodeDetector()

a = "none"

while True:
    _, img = cap.read()

    data, bbox, _ = detector.detectAndDecode(img)

    if data:
        if db.check(str(data)):
            communicate(time.time())
            print("Cod valid!")


    cv2.imshow("QR Scanner", img)

    if cv2.waitKey(1) == ord("q"):
        break



cap.release()
cv2.destroyAllWindows()
