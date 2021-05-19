import cv2
import numpy as np
from matplotlib import pyplot as plt

def flip(img,direction:str):
    """

    :param img: opencv格式图像
    :param direction: 方向,字符串形式,可选 h, v, 默认镜像
    :return: 翻转后的图像
    """
    if direction == 'h':
        flipped = cv2.flip(img,1)
    elif direction == 'v':
        flipped = cv2.flip(img,0)
    else:
        flipped = cv2.flip(img,-1)

    return flipped

def bgr2rgb(img):
   """将BGR转成RGB"""
   return cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

if __name__ == '__main__':
    img = cv2.imread('cat.jpg')

    flip_h = flip(img,'h')
    flip_v = flip(img,'v')
    flip_hv = flip(img,'hv')

    plt.subplot(221)
    plt.title('SRC')
    plt.imshow(bgr2rgb(img))

    plt.subplot(222)
    plt.title('horizontal')
    plt.imshow(bgr2rgb(flip_h))

    plt.subplot(223)
    plt.title('vertical')
    plt.imshow(bgr2rgb(flip_v))

    plt.subplot(224)
    plt.title('horAndVer')
    plt.imshow(bgr2rgb(flip_hv))

    plt.show()