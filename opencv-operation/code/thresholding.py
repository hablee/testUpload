import cv2
from matplotlib import pyplot as plt

img_path="../images/full.jpg"
img=cv2.imread(img_path)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow('w',img)
# cv2.waitKey(0)
ret1,thresh1=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
ret2,thresh2=cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)
ret3,thresh3=cv2.threshold(gray,127,255,cv2.THRESH_TRUNC)
ret4,thresh4=cv2.threshold(gray,127,255,cv2.THRESH_TOZERO)
ret5,thresh5=cv2.threshold(gray,127,255,cv2.THRESH_TOZERO_INV)

titles=['original','BINARY','BINARY_INY','TRUNC','TOZERO','TOZERO_INV']
images=[gray,thresh1,thresh2,thresh3,thresh4,thresh5]
plt.figure(figsize=(15,5))
for i in range(6):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.axis('off')
plt.show()


