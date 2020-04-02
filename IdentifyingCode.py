'''
@Author: your name
@Date: 2020-03-28 20:56:57
@LastEditTime: 2020-03-30 21:36:28
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Find-Something/IdentifyingCode.py
'''

#usr/bin/env python3

import cv2 as cv

if __name__ == "__main__":
    image = cv.imread("./3.jpg")

    # 卷积核
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3,3), (-1,-1))
    # 灰度图
    img = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    # 自动二值化
    img = cv.threshold(img, 0, 255, cv.THRESH_OTSU)[1]
    
    # 开操作（去除孤立的黑点）
    img = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
    # 膨胀（去除孤立的黑点）
    img = cv.dilate(img, kernel)
    # 腐蚀（扩大黑色的块）
    img = cv.erode(img, kernel)
    img = cv.erode(img, kernel)
    img = cv.erode(img, kernel)

    # 轮廓
    (point, valueType) = cv.findContours(img.copy(), cv.RETR_CCOMP, cv.CHAIN_APPROX_SIMPLE)
    cv.drawContours(image, point, -1, (0,0,255), 3)  # -1 所有轮廓

    rectPoint = []
    for i in point[0]:
        # Area = cv.contourArea(i)                             # 面积
        # 外接矩形
        (x, y, w, h) = cv.boundingRect(i)
        rectPoint.append((x, y, w, h))
        # cv.rectangle(image, (x, y), (x + w, y + h), (0, 150, 0), 3)

    # 去除一些轮廓
    if len(rectPoint) > 0:
        for (x,y,w,h) in rectPoint:
            print(x,y,w,h)
            # 通过轮廓长宽比，宽高范围，找到有价值的区域
            # if(1 < w/float(h) < 200):
            cv.rectangle(img, (x, y), (x + w, y + h), (0, 150, 0), 3)

    cv.imshow("image", image)
    cv.waitKey(30000)
    cv.destroyAllWindows()

