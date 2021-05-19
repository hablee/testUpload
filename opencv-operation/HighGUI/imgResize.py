import cv2
import numpy as np

"""
感觉线性插值更好
"""

def resize_func1(img):
    resized = cv2.resize(img, new_dimention,interpolation=cv2.INTER_LINEAR)
    return resized

def resize_func2(img):
    """指定缩放因子方式"""
    # resized2 = cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_NEAREST)
    resized2 = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
    return resized2

def resize_func3(img):
    dst = np.zeros((100,100,3),dtype='uint8')
    cv2.resize(img,dst=dst,dsize=(dst.shape[1],dst.shape[0]),fx=1.5,fy=2,interpolation=cv2.INTER_AREA)

    return dst


if __name__ == '__main__':
    img = cv2.imread('cat.jpg')
    height, width, channel = img.shape

    # 声明新的维度
    new_dimention = (400,400)
    resized1 = resize_func1(img)
    resized2 = resize_func2(img)
    resized3 = resize_func3(img)


    cv2.imwrite('cat_resize1.jpg',resized1)
    cv2.imwrite('cat_resize2.jpg', resized2)
    cv2.imwrite('cat_resize3.jpg', resized3)

