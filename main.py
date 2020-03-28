'''
@Author: your name
@Date: 2020-03-17 18:57:04
@LastEditTime: 2020-03-28 20:54:50
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /findDemo/main.py
'''

#usr/bin/env python3

import os
import argparse

import cv2 as cv
import numpy as np

'''
@description: 绘制矩形框
@param {type} 
@return: 
'''
def draw_rect(frame, leftUpPoiint, rightDownPoint):
    cv.rectangle(frame, leftUpPoiint, rightDownPoint, (0,128,0), 3)

'''
@description: 图片数据（矩阵转字符串）
@param {type} 
@return: 
'''
def frame_to_string(frame):
    ret, img = cv.imencode( './1.jpg', frame)
    return np.array(img).tostring()

if __name__ == "__main__":
    # ap = argparse.ArgumentParser()
    # ap.add_argument("-i", "--image", required=True, help="image")
    # ap.add_argument("-v", "--video", required=True, help="video")
    # ap.add_argument("-c", "--camera", required=True, help="camera")
    # args = vars(ap.parse_args())

    img = cv.imread("./1.jpg")

    # cv.destroyAllWindows()
