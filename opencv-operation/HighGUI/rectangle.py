import cv2
import numpy as np

def change_background(img):
    temImg = img.copy()
    hsv = cv2.cvtColor(temImg,cv2.COLOR_BGR2HSV)
    lower_white = np.array([0,0,221]) # 白色的hsv min值
    upper_white = np.array([180,30,255]) # 白色的hsv max值
    mask = cv2.inRange(hsv,lower_white,upper_white)
    rows = mask.shape[1]
    cols = mask.shape[0]
    for i in range(rows):
        for j in range(cols):
            if mask[j,i] == 255:
                temImg[j,i] = (0,0,0)

    return temImg

def rectangelv1(contours):
    """正外接矩形"""
    temImg = img.copy()
    for cidx, cnt in enumerate(contours):
        (x,y,w,h) = cv2.boundingRect(cnt)
        # 截取ROI图像
        cv2.rectangle(temImg,(x,y),(x+w,y+h),(0,0,255),1)

        # cv2.imwrite("number_boudingrect_cidx_{}.png".format(cidx), img[y:y + h, x:x + w]) # 截图保存
    return temImg

def transform(center,size,angle):
    """将传进来旋转图像变正"""
    # horizon = True
    # if horizon:
    #     if angle < -45:
    #         angle -=270
    #     if size[0] > size[1]:
    #         w = size[0]
    #         h = size[1]
    #     else:
    #         w = size[1]
    #         h = size[0]
    height,width = img.shape[0],img.shape[1]
    M = cv2.getRotationMatrix2D(center,-angle,1)
    img_rot = cv2.warpAffine(img,M,(width,height))
    (wid,hei) = size[0],size[1]
    img_crop = cv2.getRectSubPix(img_rot,(hei,wid),center) # 如果是要逆时针旋转,则调换wid和hei的位置
    cv2.imshow('ww',img_crop)
    cv2.moveWindow('ww',800,400)
    cv2.waitKey(0)

def transform2(width,height,recnt):
    if width>height:
        w = width
        h = height
    else:
        w = height
        h = width
    src_pts = recnt.astype("float32")
    dst_pts = np.array([[w-1,h-1],[0,h-1],[0,0],[w-1,0]],dtype="float32")
    M = cv2.getPerspectiveTransform(src_pts,dst_pts)
    warped = cv2.warpPerspective(img,M,(int(w),int(h)))
    cv2.imshow('res',warped)
    cv2.moveWindow('res',800,400)
    cv2.waitKey(0)



def rectangelv2(contours):
    """最小外接矩形"""
    temImg = img.copy()
    for cidx, cnt in enumerate(contours):
        """ theta是水平轴逆时针旋转，与碰到的矩形的第一条边的夹角，
            并且这个边的边长是width，另一条边长是height。也就是说这里的width和height
            并不是按长短来定义的
            (cx,cy)是中心点
        """
        ((cx, cy), (width, height), theta) = cv2.minAreaRect(cnt)

        # print('center: cx=%.3f, cy=%.3f, width=%.3f, height=%.3f, roate_angle=%.3f' % (cx, cy, width, height, theta))
        minAreaRect = ((cx, cy), (width, height), theta)
        center,size,angle = minAreaRect[0],minAreaRect[1],minAreaRect[2]
        center,size = tuple(map(int,center)),tuple(map(int,size))
        rectCnt = np.int64(cv2.boxPoints(minAreaRect)) # 这是4个顶点


        leftPointX,rightPointX = np.min(rectCnt[:,0]),np.max(rectCnt[:,0])
        topPointY, bottomPointY = np.min(rectCnt[:, 1]), np.max(rectCnt[:, 1])

        leftPointY = rectCnt[:,1][np.where(rectCnt[:,0]==leftPointX)][0]
        rightPointY = rectCnt[:,1][np.where(rectCnt[:,0]==rightPointX)][0]

        topPointX = rectCnt[:,0][np.where(rectCnt[:,1]==topPointY)][0]
        bottomPointX = rectCnt[:, 0][np.where(rectCnt[:, 1] == bottomPointY)][0]

        points = [leftPointX,leftPointY,bottomPointX,bottomPointY,rightPointX,rightPointY,topPointX,topPointY]


        transform(center,size,angle)
        # transform2(width,height,rectCnt)

        # print(leftPointX,leftPointY,bottomPointX,bottomPointY,rightPointX,rightPointY,
        #       topPointX,topPointY)

        cv2.drawContours(temImg,[rectCnt],0,(0,0,255),1)

    return temImg

if __name__ == '__main__':
    img = cv2.imread('out_renctangle.png')
    """转成黑色背景"""
    blackImg = change_background(img)
    # to gray
    gray = cv2.cvtColor(blackImg,cv2.COLOR_BGR2GRAY)
    # find contours
    """为什么只有黑色背景的图片才可以"""
    contours, hier = cv2.findContours(gray,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    img_v1 = rectangelv1(contours)
    img_v2 = rectangelv2(contours)

    # cv2.imshow('imgv1',img_v1)
    cv2.imshow('imgv2', img_v2)
    cv2.waitKey(0)

