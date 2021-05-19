import cv2


def update(x):
    """回调函数,更新value的值"""
    global value
    r_value = cv2.getTrackbarPos('R','image_win')
    g_value = cv2.getTrackbarPos('G','image_win')
    b_value = cv2.getTrackbarPos('B','image_win')

    value = (r_value,g_value,b_value)

    print('Update Value, value = {}'.format(value))




if __name__ == '__main__':
    cv2.namedWindow('image_win')
    value = (0,0,0)
    cv2.createTrackbar('R','image_win',0,255,update)
    cv2.createTrackbar('G', 'image_win', 0, 255, update)
    cv2.createTrackbar('B', 'image_win', 0, 255, update)

    cv2.setTrackbarPos('R','image_win',125)
    cv2.setTrackbarPos('G', 'image_win', 125)
    cv2.setTrackbarPos('B', 'image_win', 125)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
