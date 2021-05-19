import numpy as np
import cv2
from HighGUI.rectangle  import change_background

imgOR = cv2.imread('test1.png')
img = change_background(imgOR)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

mode = cv2.RETR_TREE
contours, hierarchy = cv2.findContours(gray,mode,method=cv2.CHAIN_APPROX_SIMPLE)
print(contours)

for idx, cnt in enumerate(contours):
    tempImg = cv2.drawContours(imgOR, [cnt],0,(0,255,0),3)
    cv2.imshow('canvas',tempImg)
    cv2.waitKey(0)

cv2.imshow('w',tempImg)
cv2.waitKey(0)

