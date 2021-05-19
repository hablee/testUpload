import numpy as np
import cv2

cap = cv2.VideoCapture('../images/v1.mp4')
# 视频每秒传输帧数
fps = cap.get(cv2.CAP_PROP_FPS)
# 视频图像宽度、高度
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(fps)
print(frame_width,frame_height)

while True:
    # ret，布尔型，表示读取成功或失败
    # frame，读取到的数据
    ret, frame = cap.read()
    if ret == False:
        break
    cv2.imshow('frame', frame)
    # waitKey功能是不断刷新图像，单位ms，返回值是当前键盘按键值
    # ord返回对应的ascii数值

    """获取每一帧的宽和高"""
    width = cap.get(3)
    height = cap.get(4)
    print(width, height)

    if cv2.waitKey(25) & 0xff == ord('q'):
        break
