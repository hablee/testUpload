import cv2
import numpy as np

def createCanvas(width,height,color=(127,127,127)):
    """创建画布"""
    canvas = np.ones((width,height,3),dtype='uint8')
    canvas[:] = color

    return canvas

def plotLine(img,pt1,pt2,color=(0,0,255),thick=1):
    cv2.line(img,pt1,pt2,color,thick)

if __name__ == '__main__':
    COLOR_MAP = {
        "green":(0,255,0),
        "red":(0,0,255)
    }
    canvas = createCanvas(400,400)
    plotLine(canvas,(0,0),(300,300),COLOR_MAP["green"],thick=2)
    plotLine(canvas,(300,0),(0,300),COLOR_MAP["red"],2)

    cv2.imshow('plotCanvas',canvas)
    cv2.waitKey(0)


