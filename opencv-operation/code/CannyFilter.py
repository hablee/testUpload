import cv2
import matplotlib.pyplot as plt

"""canny边缘检测"""
img_path="../images/full.jpg"

def edge_detect(img_path,minVal=100,maxVal=200):
    img=cv2.imread(img_path,cv2.COLOR_BGR2GRAY)
    edges=cv2.Canny(img,minVal,maxVal)
    plt.imshow(edges,'gray')
    plt.axis('off')
    plt.show()

edge_detect(img_path)








