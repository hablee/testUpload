import cv2
import numpy as np


def updateColor(x):
    canvas[:, :, 0] = cv2.getTrackbarPos('Blue', 'image')
    canvas[:, :, 1] = cv2.getTrackbarPos('Green', 'image')
    canvas[:, :, 2] = cv2.getTrackbarPos('Red', 'image')

    cv2.imshow('image',canvas)


if __name__ == '__main__':
    canvas = np.zeros((500,400,3),np.uint8) # 3通道,BGR
    # 色块的颜色
    color = (0,0,0)
    cv2.namedWindow('image')
    cv2.createTrackbar('Blue','image',0,255,updateColor)
    cv2.createTrackbar('Green', 'image', 0, 255, updateColor)
    cv2.createTrackbar('Red', 'image', 0, 255, updateColor)


    cv2.waitKey(0)

