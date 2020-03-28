'''
@Author: your name
@Date: 2020-03-19 21:37:40
@LastEditTime: 2020-03-28 20:37:55
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /findDemo/FaceManager.py
'''

#usr/bin/env python3

import os

import cv2 as cv

classfier = cv.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")

'''
@description: 人脸识别
@param {type} 
@return: 
'''
def get_face(frame):
    global classfier
    image = cv.cvtColor(frame, cv.COLOR_BGR2BGRA)
    '''
        def detectMultiScale(image, scaleFactor, minNeighbors, flags, minSize, maxSize)
        scaleFactor：在前后两次相继的扫描中，搜索窗口的比例系数。默认为1.1即每次搜索窗口依次扩大10%
        minNeighbors：构成检测目标的相邻矩形的最小个数(默认为3个)， 如果组成检测目标的小矩形的个数和小于 min_neighbors - 1 都会被排除
        flags：要么使用默认值，要么使用CV_HAAR_DO_CANNY_PRUNING，如果设置为，CV_HAAR_DO_CANNY_PRUNING，那么函数将会使用Canny边缘检测来排除边缘过多或过少的区域
        minSize：目标区域
        maxSize：目标区域
    '''
    faceRects = classfier.detectMultiScale(image, 1.1, 3)
    for (x,y,w,h) in faceRects:
        cv.rectangle(frame, (x,y), (x+w,y+h), (0,128,0), 3)
