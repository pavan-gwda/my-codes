# -*- coding: utf-8 -*-
"""
Created on Sun May  5 11:56:04 2019

@author: Pavan S Gowda
"""

import numpy as np 
import cv2 as cv

face=cv.CascadeClassifier('haarcascade_frontalface_default.xml')
eye=cv.CascadeClassifier('haarcascade_eye.xml')

img=cv.imread('fg.jpg')

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

faces=face.detectMultiScale(gray,1.3,5)

cap=cv.VideoCapture(0)

for(x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray=gray[y:y+h, x:x+w]
    roi_color=img[y:y+h,x:x+w]
    eyes=eye.detectMultiScale(roi_gray)
    for(ex,ey,ew,eh) in eyes:
        cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
cv.imshow('img',img)
cv.waitKey(0)
cv.destroyAllWindow()
    