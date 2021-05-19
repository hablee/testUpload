import cv2

img = cv2.imread('cat.jpg',cv2.IMREAD_COLOR) # 彩色
cv2.imshow('color',img)

imgGray = cv2.imread('cat.jpg',cv2.IMREAD_GRAYSCALE) # 灰度图
cv2.imshow('gray',imgGray)

cv2.waitKey(0)