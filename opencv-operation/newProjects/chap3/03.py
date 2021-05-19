import cv2
import numpy as np
from pyzbar.pyzbar import decode

imgPath = '1.png'
img = cv2.imread(imgPath)

# code = decode(img)
# print(code)
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

while True:
    success, img = cap.read()
    for barcode in decode(img):
        # print(barcode.data)
        # print(barcode.rect)
        myData = barcode.data.decode('utf-8')
        print(myData)
        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,(255,0,255),5)
        pts2 = barcode.rec
        cv2.putText(img,myData,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_COMPLEX,
                    0.9,(255,0,255),2)

        
    cv2.imshow('result',img)
    cv2.waitKey(1)

