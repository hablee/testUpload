from matplotlib import pyplot as plt
import cv2

if __name__ == '__main__':
    img = plt.imread('test1.png')
    b,g,r = cv2.split(cv2.imread('test1.png'))

    plt.subplot(2,2,1)
    plt.title('origin')
    plt.imshow(img)

    plt.subplot(2, 2, 2)
    plt.title('blue channel')
    plt.imshow(b,cmap='Blues')

    plt.subplot(2, 2, 3)
    plt.title('green channel')
    plt.imshow(b, cmap='Greens')

    plt.subplot(2, 2, 4)
    plt.title('red channel')
    plt.imshow(b, cmap='Reds')

    plt.show()
