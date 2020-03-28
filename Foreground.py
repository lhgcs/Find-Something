'''
@Author: your name
@Date: 2020-03-19 22:03:01
@LastEditTime: 2020-03-19 22:03:01
@LastEditors: your name
@Description: In User Settings Edit
@FilePath: /findDemo/forware.py
'''

#usr/bin/env python3

import cv2 as cv

mog2Frame = None
mog2 = cv.createBackgroundSubtractorMOG2() # 创建一个背景对象 黑色为背景，白色为前景
knn = cv.createBackgroundSubtractorKNN()
# 进行建模场景的时间长度，高斯混合成分的数量，阈值
# 检测阴影。如果 detectShadows = True(默认值)，它就会检测并将影子标记出来，但是这样做会降低处理速度。影子会被标记为灰色。

'''
@description: 提取前景色
@param {type} 
@return: 
'''
def get_forward(frame):
    global mog2Frame, mog2
    mog2Frame = mog2.apply(frame) # 前景的掩模
    # 开操作，去除椒盐噪声
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3,3), (-1,-1))
    # dst = cv.morphologyEx(mog2Frame,cv.MORPH_OPEN,kernel)
    dst=cv.erode(mog2Frame, kernel) # 腐蚀