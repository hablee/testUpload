import cv2
import numpy as np

def InitCanvas(width,height,color=(255,255,255)):
    canvas = np.ones((height,width,3),dtype='uint8')
    canvas[:] = color

    return canvas


if __name__ == '__main__':
    canvas = InitCanvas(300,300)

    # 绘制一个绿色圆
    cv2.circle(canvas,center=(150,150),radius=50,color=(0,255,0))
    # 增加线宽
    cv2.circle(canvas,(150,150),60,(0,0,255),5)
    # 实心圆
    cv2.circle(canvas,(150,150),30,(255,0,0),-1)

    cv2.imshow('canvas',canvas)
    cv2.waitKey(0)