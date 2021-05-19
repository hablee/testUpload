import cv2


def imgRead(img_path):
    """读取图像"""
    imgCV = cv2.imread(img_path)
    return imgCV

def lineRead(location_path):
    """读取位置文件,location: (x1,y1,x2,y2)"""
    locs = []
    for line in open(location_path):
        locs.append(line.strip())

    return locs

def screenShot(img,locs,savePath):
    """截图并保存图片"""
    for locStr in locs:
        img_loc = locStr.split(',') # 字符串列表
        print(img_loc)
        ymin, ymax ,xmin, xmax = int(img_loc[1]),int(img_loc[3]),int(img_loc[0]),int(img_loc[2])

        img_crop = img[ymin:ymax,xmin:xmax]
        cv2.imwrite(savePath +img_loc[4]+'.bmp',img_crop)


if __name__ == '__main__':
    """读取图像"""
    img_path = '../images/ImageC.bmp' # 注意和txt对齐
    img = imgRead(img_path)


    """读取位置信息"""
    loc_path = './testloc2.txt' # 注意和img_path对齐
    locs = lineRead(loc_path)

    """根据位置信息分割图像并存储"""
    import os
    save_path = 'IMG1/'
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    screenShot(img,locs,save_path)