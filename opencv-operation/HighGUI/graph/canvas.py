import cv2
import numpy as np

def InitCanvas(width,height,color=(255,255,255)):
    """创建空白画布"""
    canvas = np.ones((height,width,3),dtype="uint8")
    """第一种创建彩色图方法"""
    # (b,g,r) = cv2.split(canvas) # 分离3通道
    # b *=color[0]
    # g *=color[1]
    # r *=color[2]
    """第二种创建彩色图方法"""
    # canvas[:,:,0] = color[0]
    # canvas[:,:,1] = color[1]
    # canvas[:,:,2] = color[2]
    """第三种创建彩色图方法"""
    canvas[:] = color

    # return cv2.merge([b,g,r])
    return canvas

if __name__ == '__main__':
    canvas = InitCanvas(200,200,color=(127,127,127))

    cv2.imshow("canvas",canvas)
    cv2.waitKey(0)

