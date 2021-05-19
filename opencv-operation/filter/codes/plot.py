from matplotlib import pyplot as plt


img_path = '../images/Image_20210507174336622.bmp'
img = plt.imread(img_path)
print(img.shape)
plt.imshow(img,cmap=plt.cm.gray)
plt.show()

# 1897,1045,1992,1140