import cv2
import numpy as np

#############################
widthImg = 640
heightImg = 480
nPlateCascade = cv2.CascadeClassifier('../resource/haarcascade_russian_plate_number.xml')
minArea = 500
color = (255,0,255)
#############################

cap = cv2.VideoCapture(1)
cap.set(3,widthImg)
cap.set(4,heightImg)
cap.set(10,150)
count = 0

while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    numberPlates = nPlateCascade.detectMultiScale(imgGray, 1.1, 4)
    for (x,y,w,h) in numberPlates:
        area = w*h
        if area > minArea:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.putText(img,"number plate",(x,y-5),
                        cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)
            imgRoi = img[y:y+h,x:x+w]
            cv2.imshow("ROI",imgRoi)


    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF==ord('s'):
        cv2.imwrite("Resources/scanned/NoPlate_"+str(count)+".jpg",imgRoi)
        cv2.rectangle(img,(0,200),(640,300),(0,255,0),cv2.FILLED)
        cv2.putText(img,"Scan Saved",(150,265),cv2.FONT_HERSHEY_DUPLEX,
                    2,(0,0,255),2)
        cv2.imshow("Result",img)
        count += 1

