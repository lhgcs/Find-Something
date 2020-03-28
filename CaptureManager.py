'''
@Author: your name
@Date: 2020-03-19 21:35:23
@LastEditTime: 2020-03-28 20:33:46
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /findDemo/CaptureManager.py
'''

#usr/bin/env python3

import os

import cv2 as cv
import numpy as np

'''
@description: 读取视频文件
@param {type} 
@return: 
'''
def read_video_file(fileName, callback):
    if not os.path.exists(fileName):
        print("can not find", fileName)
        return
    
    cap = cv.VideoCapture(fileName)
    if cap is None:
        print("can not open")
        return

    while True:
        res, frame = cap.read()
        if res:
            callback(frame)
        else:
            break

        if cv.waitKey(10) > 0:
            break

    cap.release()
    cap = None
    