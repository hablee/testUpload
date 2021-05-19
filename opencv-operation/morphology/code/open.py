import cv2
import numpy as np

img = cv2.imread('./IMG1/l.bmp')
g=cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
img_open=cv2.morphologyEx(img,cv2.MORPH_OPEN,g)
cv2.imshow('img_open',img_open)
cv2.imwrite('img.bmp',img_open)
cv2.waitKey(0)

