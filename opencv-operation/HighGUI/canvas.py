import numpy as np
import cv2

def createGrayscaleCanvas(width, height, color=255):
    canvas = np.ones((height,width),dtype='uint8')
    canvas[:] = color
    return canvas

def is_gvalue_legal(gvalue):
    return not (gvalue<0 or gvalue>255)

def read_gvalue():
    read_done = False
    gvalue = None

    while not read_done:
        gvalue_str = input("请输入灰度值:")
        gvalue = int(gvalue_str)
        read_done = is_gvalue_legal(gvalue)
        if read_done == False:
            print("灰度图值必须在0-255之间")

    return gvalue


def nothing(x):
    """被传入的x是滑条的当前取值"""
    print(x)

def updateImg(gvalue):
    img = createGrayscaleCanvas(500,500,color=gvalue)
    cv2.imshow('canvas',img)

if __name__ == '__main__':
    # gvalue = read_gvalue()
    # canvas = createGrayscaleCanvas(500,500,color=125)
    # cv2.imshow('canvas',canvas)
    cv2.namedWindow('canvas')
    updateImg(0)
    cv2.createTrackbar('gray_value','canvas',0,255,updateImg)

    while cv2.waitKey(0) != ord('q'):
        """按q退出"""
        continue

    cv2.destroyAllWindows()