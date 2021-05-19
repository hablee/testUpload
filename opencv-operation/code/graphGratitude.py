import cv2
import matplotlib.pyplot as plt

"""图像梯度"""
img_path="../images/full.jpg"
img=cv2.imread(img_path)

def gradient(image):
    image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    # cv2.CV_64F输出图像深度(数据类型),644位float类型
    laplacian=cv2.Laplacian(image,cv2.CV_64F)
    # 1,0表示在x方向求一阶导数，最大可以求2阶
    sobelx=cv2.Sobel(image,cv2.CV_64F,1,0,ksize=3)
    # 0,1表示在y方向求一阶导数，最大可以求2阶
    sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
    titles=['Original','Laplacian','SobelX','SobelY']
    images=[image,laplacian,sobelx,sobely]
    plt.figure(figsize=(10,5))
    for i in range(4):
        plt.subplot(2,2,i+1)
        plt.imshow(images[i],'gray')
        plt.title(titles[i])
        plt.axis('off')
    plt.show()

gradient(img)

