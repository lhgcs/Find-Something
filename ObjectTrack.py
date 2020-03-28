'''
@Author: your name
@Date: 2020-03-28 21:00:08
@LastEditTime: 2020-03-28 23:14:25
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Find-Something/ObjectTrack.py
'''

#usr/bin/env python3

import cv2 as cv

'''
@description: 获取轮廓
@param {type} 
@return: 
'''
def get_rect(image):
    rectPoint = []
    img = cv.cvtColor(image, cv.COLOR_BGR2GRAY)           # 灰度图
    img = cv.threshold(img, 0, 255, cv.THRESH_OTSU)[1]    # 自动二值化
    # img = cv.morphologyEx(img, cv.MORPH_OPEN, (1,1))  
    (point, valueType) = cv.findContours(img, cv.RETR_CCOMP, cv.CHAIN_APPROX_SIMPLE) # 检测外轮廓

    for i in point:
        print("i:",i)
        cv.drawContours(image, i, -1, (0, 150, 0), 3)  
        # Area = cv.contourArea(i)                             # 面积
        (x, y, w, h) = cv.boundingRect(i)                    # 外接矩形
        rectPoint.append((x, y, w, h))
    return rectPoint    

if __name__ == "__main__":
    img = cv.imread("./2.jpg")
    rectPoint = get_rect(img)

    if len(rectPoint) > 0:
        for (x,y,w,h) in rectPoint:
            # 通过轮廓长宽比，宽高范围，找到有价值的区域
            if(1 < h * 1.0 / w < 1.2):
                cv.rectangle(img, (x, y), (x + w, y + h), (0, 150, 0), 3)

    cv.imshow("image", img)
    cv.waitKey(3000)