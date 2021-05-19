import cv2
import os

locs = [[282,238,323,283,'a'],[262,408,303,453,'b']]

img_path = '../image/connect0517Rs_0008.jpg'

save_path = './IMGCrop/'
if not os.path.exists(save_path):
        os.makedirs(save_path)
else:
    print("文件夹已存在")

img = cv2.imread(img_path)

for loc in locs:
    crop = img[loc[1]:loc[3],loc[0]:loc[2]]
    cropGray = cv2.cvtColor(crop,cv2.COLOR_BGR2GRAY)

    # ret, binary = cv2.threshold(cropGray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    ret, binary = cv2.threshold(cropGray, 60, 255, cv2.THRESH_BINARY)

    print("threshold value %s" % ret)  # 打印阈值，超过阈值显示为白色，低于该阈值显示为黑色
    cv2.imshow("threshold", binary)  # 显示二值化图像
    cv2.moveWindow("threshold",800,400)
    cv2.waitKey(0)

    cv2.imwrite(save_path+loc[4]+'.jpg',binary)



