import cv2
import numpy as np

def InitCanvas(width,height,color=(255,255,255)):
    canvas = np.ones((height,width,3),dtype='uint8')
    canvas[:] = color

    return canvas

def plot_rectangle(img,pt1:tuple,pt2:tuple,color=(127,127,127),thick=2):
    cv2.rectangle(img,pt1,pt2,color,thick)

if __name__ == '__main__':
    COLOR_MAP = {
        "white":(255,255,255),
        "green":(0,255,0),
        "red":(0,0,255),
        "blue":(255,0,0),
    }

    canvas = InitCanvas(400,400,COLOR_MAP["white"])
    plot_rectangle(canvas,(10,10),(60,60),COLOR_MAP["red"])
    plot_rectangle(canvas,(50,200),(200,225),COLOR_MAP["green"],5)
    # thick为-1表示填充矩形
    plot_rectangle(canvas,(200,50),(225,125),COLOR_MAP["blue"],-1)

    cv2.imshow('canvas',canvas)
    cv2.waitKey(0)
