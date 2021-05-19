import cv2


def update(x):
    # 回调函数,更新value的值
    global value
    value = x
    print('Update Value, value = {}'.format(value))

if __name__ == '__main__':
    cv2.namedWindow('image_win')
    value = None
    cv2.createTrackbar('value_name','image_win',60,505,update)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

