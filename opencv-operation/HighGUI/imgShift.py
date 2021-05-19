import cv2
import numpy as np


def translate(img,x:int,y:int):
    """
    :param img: 图像
    :param x: 向右平移多少
    :param y: 向下平移多少
    :return: img
    """
    M = np.float32([[1,0,x],[0,1,y]])
    shifted = cv2.warpAffine(img,M,(img.shape[1],img.shape[0]))
    return shifted

if __name__ == '__main__':
    img = cv2.imread('cat.jpg')

    for x,y in zip(range(10,30,10),range(30,10,-10)):
        print(x,y)
        shifted = translate(img,x,y)
        cv2.imshow('shift',shifted)
        cv2.waitKey(0)


