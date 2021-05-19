import numpy as np
import cv2

cap = cv2.VideoCapture('../images/v1.mp4')
# 视频每秒传输帧数
fps = cap.get(cv2.CAP_PROP_FPS)
# 视频图像宽度、高度
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('../images/output.avi',fourcc,fps,(frame_width,frame_height))

while True:
    ret,frame = cap.read()
    if ret==True:
        # 水平翻转
        frame = cv2.flip(frame,1)
        out.write(frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xff == ord('q'):
            break
    else:
        break

out.release()
cap.release()
cv2.destroyAllWindows()