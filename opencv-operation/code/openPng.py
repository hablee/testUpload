"""查看图片保存的是不是深度值"""
import cv2
import matplotlib.pyplot as plt
import numpy as np

img_path='D:\mechImages/mechmind_depth.png'
img_cv=cv2.imread(img_path)
img_plt=plt.imread(img_path)
plt.imshow(img_plt)
plt.show()

png_arry=np.array(img_cv)
for i in range(610,799): # 里面的范围你可以自己定义
    for j in range(139,610): # 里面的范围你可以自己定义
        print(png_arry[i,j])
