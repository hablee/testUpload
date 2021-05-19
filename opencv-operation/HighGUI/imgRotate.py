import cv2
import numpy as np
from math import cos,sin,radians
from matplotlib import pyplot as plt

def rotate(img,angle:int,center=None,scale=1.0):
    """

    :param img: 图像
    :param angle: 角度，逆时针方向为正方向（正值）
    :param center:
    :param scale: 缩放倍数，1.0表示尺寸不变
    :return:
    """
    (h,w) = img.shape[:2]
    if center is None: # 默认参数
        center = (w/2, h/2)

    M = cv2.getRotationMatrix2D(center,angle,scale)
    rotated = cv2.warpAffine(img,M,(w,h))

    return rotated


if __name__ == '__main__':
    img = cv2.imread('cat.jpg')
    height, width, channel = img.shape

    cx = int(width/2)
    cy = int(height/2)
    center = (cx,cy)

    new_dim = (width,height)

    rotate30 = rotate(img,30,(0,0)) # 绕原点逆时针转30度
    cv2.imshow('rotate30',rotate30)
    cv2.moveWindow('rotate30',800,400)
    cv2.waitKey(0)

    rotate30 = rotate(img, 30)  # 绕中心逆时针转30度
    cv2.imshow('rotate45', rotate30)
    cv2.moveWindow('rotate30', 800, 400)
    cv2.waitKey(0)


