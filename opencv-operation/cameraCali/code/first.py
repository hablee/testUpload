import cv2
import numpy as np
import glob

# 标定图像
'''
标定步骤：
1）
'''


def calibration_photo(photo_path):
    # 设置要标定的角点个数（我这里使用的是11 × 8的棋盘，11×8代
    # 表的是内角点，这里要注意，不懂的话可以数数我拍摄的棋盘你就知道哪个是内角点了）
    x_nums = 11  # x方向上的角点个数
    y_nums = 8
    # 设置(生成)标定图在世界坐标中的坐标
    world_point = np.zeros((x_nums * y_nums, 3), np.float32)  # 生成x_nums*y_nums个坐标，每个坐标包含x,y,z三个元素
    world_point[:, :2] = 15 * np.mgrid[:x_nums, :y_nums].T.reshape(-1,
                                                                   2)  # mgrid[]生成包含两个二维矩阵的矩阵，每个矩阵都有x_nums列,y_nums行，我这里用的是15mm×15mm的方格，所以乘了15，以mm代表世界坐标的计量单位
    print(world_point)  # 打印出来的就是某一张出图片的世界坐标了
    # .T矩阵的转置
    # reshape()重新规划矩阵，但不改变矩阵元素
    # 保存角点坐标
    world_position = []  # 存放世界坐标
    image_position = []  # 存放棋盘角点对应的图片像素坐标

    '''
    下面就是查找图片中角点的像素坐标存入image_position了
    '''

    # 设置角点查找限制
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
    # 获取所有标定图
    images = glob.glob(photo_path + '\\*.bmp')
    # print(images)
    for image_path in images:
        image = cv2.imread(image_path)
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        # 查找角点
        ok, corners = cv2.findChessboardCorners(gray, (x_nums, y_nums), None)
        """
		如果能找得到角点：返回角点对应的像素坐标，并且将其对应到世界坐标中
		世界坐标[0,0,0],[0,1,0].....
		图像坐标[10.123123,20.123122335],[19.123123,21.123123123]....
        """
        if ok:
            # 把每一幅图像的世界坐标放到world_position中
            world_position.append(world_point)
            # 获取更精确的角点位置
            exact_corners = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
            # 把获取的角点坐标放到image_position中
            image_position.append(exact_corners)
            # 可视化角点
            image = cv2.drawChessboardCorners(image, (x_nums, y_nums), exact_corners, ok)
            cv2.imshow('image_corner', image)
            cv2.waitKey(1)

    """
    点对应好了，开始计算内参，畸变矩阵，外参
    """
    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(world_position, image_position, gray.shape[::-1], None, None)
    # 内参是mtx，畸变矩阵是dist，旋转向量（要得到矩阵还要进行罗德里格斯变换）rvecs，外参：平移矩阵tvecs
    # 将内参保存起来
    np.savez('./checkerboard', mtx=mtx, dist=dist)

    print('内参是：\n', mtx, '\n畸变参数是：\n', dist,
          '\n外参：旋转向量（要得到矩阵还要进行罗德里格斯变换，下章讲）是：\n', rvecs, '\n外参：平移矩阵是：\n', tvecs)

    # 计算偏差
    mean_error = 0
    for i in range(len(world_position)):
        image_position2, _ = cv2.projectPoints(world_position[i], rvecs[i], tvecs[i], mtx, dist)
        error = cv2.norm(image_position[i], image_position2, cv2.NORM_L2) / len(image_position2)
        mean_error += error
    print("total error: ", mean_error / len(image_position))


def main():
    # 标定图像保存路径
    photo_path = "../images"
    calibration_photo(photo_path)


if __name__ == '__main__':
    main()


"""结果"""
"""
内参是：
 [[3.84374677e+03 0.00000000e+00 1.39121394e+03]
 [0.00000000e+00 3.84336387e+03 1.00267771e+03]
 [0.00000000e+00 0.00000000e+00 1.00000000e+00]] 
"""

"""
畸变参数是：
 [[-7.23660247e-02  5.11314712e-01 -2.20105485e-03  9.60831554e-03
   3.37341939e+00]] 
"""

"""
外参：旋转向量（要得到矩阵还要进行罗德里格斯变换，下章讲）是：
 [array([[-0.019167  ],
       [-0.43856956],
       [-0.31428556]]), array([[ 0.03820729],
       [-0.23927899],
       [ 0.22851135]]), array([[-0.61468098],
       [-0.01350643],
       [-0.04102546]]), array([[ 0.39151378],
       [ 0.01297959],
       [-0.18706348]]), array([[-0.00954611],
       [-0.03782357],
       [-0.02939513]]), array([[-0.05847206],
       [-0.55695914],
       [-0.10184303]]), array([[-0.15798438],
       [ 0.24417945],
       [-0.15304568]]), array([[-0.04548933],
       [ 0.00286769],
       [-0.04053741]]), array([[ 0.02112269],
       [-0.4712832 ],
       [-0.24470288]]), array([[ 0.10412314],
       [ 0.18042521],
       [-0.18770686]]), array([[-0.02710534],
       [-0.03198559],
       [-0.2815528 ]]), array([[-0.35163141],
       [ 0.09060583],
       [-0.22130174]]), array([[-0.73799143],
       [-0.01781   ],
       [ 0.02585421]]), array([[0.46074354],
       [0.01668383],
       [0.07850727]]), array([[-0.07759816],
       [ 0.43722655],
       [ 0.05905001]]), array([[0.22972686],
       [0.03903455],
       [0.13826179]])] 
"""

"""
[array([[-101.79520454],
       [ -33.59255784],
       [ 358.31707446]]), array([[-40.51152954],
       [-76.79730173],
       [369.82771331]]), array([[-80.99324152],
       [-35.27613779],
       [410.86748117]]), array([[-91.42277132],
       [-24.96251387],
       [370.91557543]]), array([[-102.30876545],
       [ -32.66638479],
       [ 451.79550286]]), array([[-88.68446292],
       [-50.49473129],
       [340.32978906]]), array([[-119.91451367],
       [ -44.00831958],
       [ 437.14709234]]), array([[-72.56718397],
       [-46.55974809],
       [417.91328418]]), array([[-100.45427346],
       [ -41.22962871],
       [ 363.67448932]]), array([[-85.10276691],
       [-37.5574248 ],
       [395.77903499]]), array([[-133.90941386],
       [ -19.96499157],
       [ 453.65884271]]), array([[-114.09229909],
       [ -25.77302926],
       [ 433.17665258]]), array([[-77.04279865],
       [-44.62207934],
       [410.17904544]]), array([[-80.51340402],
       [-44.19436573],
       [368.49240228]]), array([[-69.50509128],
       [-52.38834627],
       [414.24884205]]), array([[-67.89374582],
       [-46.82243586],
       [401.45714938]])]
"""

"""
total error:  0.25845439892954436
"""

