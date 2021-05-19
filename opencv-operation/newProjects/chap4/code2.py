import os
import cv2

"""
因为图像像素是一定的，可以按位置分割之后再拼接
"""


mainFolder = 'Images4'
folder = '4'
path = mainFolder +'/'+folder

images =[]
myList = os.listdir(path)
print(f'Total no of images detected {len(myList)}')
for imgN in myList:
    curImg = cv2.imread(f'{path}/{imgN}')
    curImg = cv2.resize(curImg,(0,0),None,0.2,0.2)
    images.append(curImg)

stitcher = cv2.Stitcher.create()
(status,result) = stitcher.stitch(images)
if (status == cv2.STITCHER_OK):
    print('Panorama Generated')
    cv2.imshow(folder,result)
    cv2.imwrite(folder+'.bmp',result)
    cv2.waitKey(1)
else:
    print('Panorama Generation Unsuccessful')

cv2.waitKey(0)