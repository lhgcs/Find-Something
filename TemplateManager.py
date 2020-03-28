'''
@Author: your name
@Date: 2020-03-19 21:45:45
@LastEditTime: 2020-03-28 20:53:17
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /findDemo/TemplateManager.py
'''

#usr/bin/env python3

import cv2 as cv

'''
匹配方法:
CV_TM_SQDIFF:平方差匹配法
CV_TM_SQDIFF_NORMED:归一化平方差匹配法
CV_TM_CCORR:相关匹配法
CV_TM_CCORR_NORMED:归一化相关匹配法
CV_TM_CCOEFF:系数匹配法
CV_TM_CCOEFF_NORMED:化相关系数匹配法
'''

'''
@description: 模板匹配
@param {type} 
@return: 
'''
def get_dst(image, imageTemplate):
    image = cv.matchTemplate(image, imageTemplate, cv.TM_CCOEFF_NORMED)
    print(image)
    # 得到矩阵的最小值，最大值
    min_val,max_val,min_index,max_index = cv.minMaxLoc(image)
    return min_index
    