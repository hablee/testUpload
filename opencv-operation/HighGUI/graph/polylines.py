import cv2
import numpy as np

def InitCanvas(width,height,color=(255,255,255)):
    canvas = np.ones((height,width,3),dtype='uint8')
    canvas[:] = color

    return canvas


if __name__ == '__main__':
    canvas = InitCanvas(800,500)
    points = np.array([[100,50],[200,300],[700,200],[500,100]],np.int32)
    # 点集矩阵变形
    print('points before shape', points.shape)
    points = points.reshape((-1,1,2))
    print('points after shape',points.shape)

    cv2.polylines(canvas,pts=[points],isClosed=True,color=(0,0,255),thickness=3)

    cv2.imshow('canvas',canvas)
    cv2.moveWindow('canvas',800,300)
    cv2.waitKey(0)