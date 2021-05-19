import cv2

faceCascade = cv2.CascadeClassifier('../resource/haarcascade_frontalface_default.xml')
img = cv2.imread('../images/lena.png')
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray,1.1,4)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.putText(img,'lena',(x-10,y-10),cv2.FONT_HERSHEY_COMPLEX,
                0.8,(0,0,255),2)

cv2.imshow("Result",img)
cv2.waitKey(0)


