import cv2
import matplotlib.pyplot as plt

img_path="../images/full.jpg"
img=cv2.imread(img_path)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
plt.imshow(gray,'gray')
plt.axis('off')
plt.show()

"""自动选取阈值,全局阈值"""
ret1,thresh1=cv2.threshold(gray,0,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)
ret2,thresh2=cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)

print('ret1: ',ret1)
print('ret2: ',ret2)

plt.imshow(thresh1,'gray')
plt.axis('off')
plt.show()

plt.imshow(thresh2,'gray')
plt.axis('off')
plt.show()