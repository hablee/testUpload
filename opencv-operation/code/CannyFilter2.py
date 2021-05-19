import cv2
import matplotlib.pyplot as plt
import numpy as np

"""canny边缘检测阈值影响"""
img_path="../images/full.jpg"
image=cv2.imread(img_path)
image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)


# image=cv2.GaussianBlur(image,(3,3),0)
# value=[(10,150),(100,200),(180,230)]
# plt.figure(figsize=(20,5))
# for i,(minVal,maxVal) in enumerate(value):
#     plt.subplot(1,3,i+1)
#     edges=cv2.Canny(image,minVal,maxVal)
#     edges=cv2.GaussianBlur(edges,(3,3),0)
#     plt.imshow(edges,'gray')
#     plt.title(str((minVal,maxVal)))
#     plt.axis('off')
# plt.show()

# 自动确定阈值的一种方法
def auto_canny(image,sigma=0.3):
    v=np.median(image)
    lower=int(max(0,(1.0-sigma)*v))
    upper=int(min(255,(1.0+sigma)*v))
    edges=cv2.Canny(image,lower,upper)
    print(lower,upper)
    return edges

edges=auto_canny(image)
edges=cv2.GaussianBlur(edges,(3,3),0)
plt.imshow(edges,'gray')
plt.axis('off')
plt.show()

