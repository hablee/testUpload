import cv2
import numpy as np

def InitCanvas(width,height,color=(255,255,255)):
    canvas = np.ones((height,width,3),dtype='uint8')
    canvas[:] = color

    return canvas



if __name__ == '__main__':
    canvas = InitCanvas(400,400)

    cv2.putText(canvas,text="hello world",org=(50,200),fontFace=cv2.FONT_HERSHEY_TRIPLEX,fontScale=1,thickness=1,lineType=cv2.LINE_AA,color=(0,0,255))

    cv2.imshow('canvas',canvas)
    cv2.waitKey(0)
