import cv2
import numpy as np

def zhi_fang_tu(img):
    # img = cv2.imread(img_path, 0)
    equ = cv2.equalizeHist(img)
    # res = np.hstack((img, equ))
    # res_resize = cv2.resize(res,(int(res.shape[1]*1),int(res.shape[0]*1)))
    cv2.imshow('img', equ)
    cv2.waitKey(0)
    return equ


def zhi_fang_tu2(img):
    # img = cv2.imread(img_path,cv2.IMREAD_ANYCOLOR)
    clahe = cv2.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))
    dst = clahe.apply(img)
    res_resize = cv2.resize(dst, (int(dst.shape[1] * 1), int(dst.shape[0] * 1)))
    cv2.imwrite('zhi_fang_tu2.bmp',res_resize)
    cv2.imshow('zhi_fang_tu2',res_resize)
    dst = cv2.cvtColor(dst,cv2.COLOR_GRAY2BGR)
    print(dst.shape)
    cv2.waitKey(0)


if __name__ == '__main__':
    img_path = '../images/Image_20210507174336622.bmp'
    # # zhi_fang_tu2(img_path)
    #
    # """低通滤波"""
    # img = cv2.imread(img_path,0)
    # img_blur = cv2.GaussianBlur(img,(5,5),9)
    # res_resize = cv2.resize(img_blur, (int(img_blur.shape[1] * 1), int(img_blur.shape[0] * 1)))
    # cv2.imshow('w',res_resize)
    # cv2.waitKey(0)
    #
    # """中值滤波"""
    # img_median = cv2.medianBlur(res_resize,3)
    # cv2.imshow('m', img_median)
    # cv2.imwrite('median.bmp',img_median)
    # cv2.waitKey(0)

    """直方图2均衡"""
    img = cv2.imread(img_path,0)
    print(img.shape)
    img_SFT = zhi_fang_tu2(img)





