
import numpy as np
"""
图像坐标：1341, 1041
"""

# """图像坐标"""
# picCo = np.mat([[1341],[1041],[1]])
# # print(picCo)
# # print(picCo.shape)
#
# """内参"""
# neican = np.mat( [[3.84374677e+03,0.00000000e+00,1.39121394e+03],
#  [0.00000000e+00,3.84336387e+03,1.00267771e+03],
#  [0.00000000e+00,0.00000000e+00,1.00000000e+00]] )
# """内参的逆矩阵"""
# neicanInverse = np.linalg.inv(neican)
# print(neicanInverse)
#
# """相机坐标系"""
# camCo = neicanInverse * picCo
# print(camCo)

# dickey = [{(1341, 1041): 17}, {(1297, 1119): 29}, {(1310, 953): 18}, {(1321, 1199): 17}, {(1033, 917): 18}, {(1276, 870): 16}, {(900, 1073): 21}, {(966, 751): 21}, {(1078, 601): 19}, {(1240, 785): 18}, {(870, 994): 28}, {(1211, 706): 29}, {(981, 1037): 17}, {(1028, 680): 27}, {(1479, 789): 27}, {(1252, 1030): 14}, {(1217, 941): 17}, {(1174, 1263): 17}, {(1054, 756): 16}, {(1176, 621): 27}, {(1406, 653): 23}]
# for item in dickey:
#     turple = list(item.keys())[0]
#     print(turple[0],turple[1])


def pic2cam(tuple):
    """矩阵运算像素坐标转相机坐标"""
    picCo = np.mat([[tuple[0]],[tuple[1]],[1]])
    # print(picCo)
    # print(picCo.shape)

    """内参"""
    neican = np.mat( [[3.84374677e+03,0.00000000e+00,1.39121394e+03],
     [0.00000000e+00,3.84336387e+03,1.00267771e+03],
     [0.00000000e+00,0.00000000e+00,1.00000000e+00]] )
    """内参的逆矩阵"""
    neicanInverse = np.linalg.inv(neican)
    # print(neicanInverse)

    """相机坐标系"""
    camCo = neicanInverse * picCo
    zc = 0.3 # 镜头到物体平面的距离,单位为m

    return camCo*zc


def depth2mi(depthValue):
    """深度值转米"""
    print('depth2mi ok')
    return depthValue * 0.001

def depth2xyz(u,v, depthValue):
    """像素坐标转相机坐标"""
    fx = 3.84374677e+03
    fy = 3.84336387e+03
    cx = 1.39121394e+03
    cy = 1.00267771e+03

    depth = depth2mi(depthValue)

    z = float(depth)
    x = float((u - cx) * z) / fx
    y = float((v - cy) * z) / fy
    """
    微软相机：
    内参矩阵
    fx = 1.82650372e+03
    fy = 1.81976419e+03
    cx = 1.95264382e+03
    cy = 1.12896011e+03
    外参矩阵
    [[ 9.90153097e-01  6.21230042e-02 -1.25449499e-01 -1.79204162e+02]
     [-5.48913040e-02  9.96669542e-01  6.03056329e-02 -1.31021582e+02]
     [1.28778062e-01  -5.28257226e-02  9.90265446e-01  3.23457877e+02]
     [0.00000000e+00  0.00000000e+00  0.00000000e+00  1.00000000e+00]]
    """
    result = [x, y, z]
    print('depth2xyz ok')
    return result



if __name__ == '__main__':
    # camCO = pic2cam((1341, 1041))
    # print(camCO[0,0],camCO[1,0],camCO[2,0])

    re1 =depth2xyz(1341, 1041,300)
    print('result in depth2value:',re1)

    re2 = pic2cam((1341, 1041))
    print('result in pic2cam:',re2)





