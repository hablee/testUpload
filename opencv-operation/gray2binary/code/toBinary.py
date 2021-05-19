import cv2

img_path = '../image/1.bmp'
img = cv2.imread(img_path,0)

ret, binary = cv2.threshold(img, 60, 255, cv2.THRESH_BINARY)
cv2.imshow('binary',binary)
cv2.moveWindow('binary',800,400)
cv2.waitKey(0)