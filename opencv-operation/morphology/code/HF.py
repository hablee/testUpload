import os
import cv2
import numpy as np

# img_paths = [
#     r"E:\jinji\0001.png",
#     r"E:\jinji\0010.jpg"
# ]
#
# for path in img_paths:
#
#     img = cv2.imread(path, 0)
#     # img = cv2.medianBlur(img,3)
#     cv2.imshow('img_o', img)
#     img = cv2.GaussianBlur(img, (3, 3), 0)
#     img = cv2.medianBlur(img, 5)
#     cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
#
#     circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 60, param1=30, param2=12, minRadius=2, maxRadius=30)
#
#     circles = np.uint16(np.around(circles))
#
#     for i in circles[0, :]:
#         # draw the outer circle
#         cv2.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 1)
#         # draw the center of the circle
#         cv2.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 1)
#
#     cv2.imshow('detected circles', cimg)
#     cv2.waitKey(0)
# cv2.destroyAllWindows()

def HFFunction(img_path):
    img = cv2.imread(img_path) # BGR
    img = cv2.pyrMeanShiftFiltering(src=img, sp=5, sr=16) # remove background
    cv2.imshow('img_o', img)
    cv2.moveWindow('img_o',800,400)

    # g = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2)) # 开运算
    # img = cv2.morphologyEx(img, cv2.MORPH_OPEN, g)

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # BGR->GRAY

    # img = cv2.equalizeHist(img)

    img = cv2.medianBlur(img, 3)
    # img = cv2.GaussianBlur(img, (5, 5), 0)
    img = cv2.medianBlur(img, 5)

    # clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    # img = clahe.apply(img)

    cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR) # Gray->BGR
    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 100, param1=100, param2=20, minRadius=1, maxRadius=20)

    if type(circles) != type(None):
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            # draw the outer circle
            cv2.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 1)
            r = i[2]
            center = (i[0], i[1])
            # draw the center of the circle
            cv2.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 1)
            print(center,r)

        cv2.imshow('detected circles', cimg)
        cv2.moveWindow('detected circles', 900, 400)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print('未检测到圆')


def function2(img_path):
    """测试去除背景代码"""
    img = cv2.imread(img_path)
    img = cv2.pyrMeanShiftFiltering(src=img, sp=5, sr=16)
    # cv2.imshow('test',img)
    # cv2.moveWindow('test',800,400)
    # print((img.shape))
    cv2.waitKey(0)

if __name__ == '__main__':
    # img_dir = 'IMG1/'
    # for filename in os.listdir(img_dir):
    #     print(filename)
    #     img_path = 'IMG1/'+filename
    #     HFFunction(img_path)
    #     function2(img_path)

    img_path = r'D:\projects\opencv-operation\gray2binary\code\IMGCrop\b.jpg'
    HFFunction(img_path)