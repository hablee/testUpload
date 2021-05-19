import cv2
import matplotlib.pyplot as plt

img_path="../images/full.jpg"
img=cv2.imread(img_path)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# 中值滤波
image=cv2.medianBlur(gray,5)
# 普通二值化
ret1,th1=cv2.threshold(image,127,255,cv2.THRESH_BINARY)
# 平均阈值
th2=cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,3)
# 高斯阈值
th3=cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,3)

titles=['original','Global Thresholding','Adaptive Mean Thresholding','Adaptive Gaussian Thresholding']
images=[image,th1,th2,th3]
plt.figure(figsize=(10,5))
for i in range(4):
    plt.subplot(2,2,i+1)
    plt.imshow(images[i],'gray')
    plt.axis('off')
    plt.title(titles[i])

plt.show()




"""自适应阈值"""

