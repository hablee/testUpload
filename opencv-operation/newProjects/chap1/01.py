from PIL import Image
import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = r"D:\Program Files\Tesseract-OCR\tesseract.exe"

imgPath = 'tess6.png'
img = cv2.imread(imgPath)
hImg, wImg, _ = img.shape

"""list"""
# boxes = pytesseract.image_to_boxes(Image.open(imgPath),lang='chi_sim')
# for box in boxes.splitlines():
#     print(box)
#     box = box.split(' ')
#     print(box)
#     x,y,w,h = int(box[1]),int(box[2]),int(box[3]),int(box[4])
#     cv2.rectangle(img,(x,hImg-y),(w,hImg-h),(0,0,255),2)
#     cv2.putText(img,box[0],(x,hImg-y-60),cv2.FONT_HERSHEY_COMPLEX,1,(50,255,50),2)



cong = r'--oem 3 --psm 6 outputbase digits'

data = pytesseract.image_to_data(Image.open(imgPath),config=cong)
# print(data)

for i,box in enumerate(data.splitlines()):
    if i != 0:
        box = box.split()
        # print(box)
        if len(box) == 12:
            x,y,w,h = int(box[6]),int(box[7]),int(box[8]),int(box[9])
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
            cv2.putText(img,box[11],(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(50,255,50),2)

cv2.imshow('result',img)
cv2.waitKey(0)




