import cv2
import matplotlib.pyplot as plt
import numpy as np


if __name__ == '__main__':
    # img = plt.imread('prosperctive.png')
    # plt.imshow(img)
    # plt.show()
    # 80,37,27,382,560,380,494,84
    img = cv2.imread('prosperctive.png')
    rows, cols, ch = img.shape
    # 4个点坐标
    pts1 = np.float32([[80,37],[494,84],[27,382],[560,380]])
    # 变换到新位置的坐标
    pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
    # 生成变换矩阵
    M = cv2.getPerspectiveTransform(pts1,pts2)
    # 进行透视变换
    dst = cv2.warpPerspective(img,M,(300,300))

    plt.subplot(121),plt.imshow(img),plt.title('input')
    plt.subplot(122),plt.imshow(dst),plt.title('output')
    plt.show()


