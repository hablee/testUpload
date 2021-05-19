import numpy as np
import cv2

cap=cv2.VideoCapture(0) # 0表示从摄像头获取数据

while True:
    # ret，布尔型，表示读取成功或失败
    # frame，读取到的数据
    ret,frame=cap.read()
    # 灰度处理
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',gray)
    # waitKey功能是不断刷新图像，单位ms，返回值是当前键盘按键值
    # ord返回对应的ascii数值

    """获取每一帧的宽和高"""
    width = cap.get(3)
    height = cap.get(4)
    print(width,height)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break



cap.release()
cv2.destroyAllWindows()


