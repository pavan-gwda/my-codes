# -*- coding: utf-8 -*-
"""
Created on Sun May  5 10:39:28 2019

@author: Pavan S Gowda
"""
import cv2
import numpy as np

#load an color image in grayscale
'''
img=cv2.imread('kl.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
cap=cv2.VideoCapture(0)

while(True):
    #capture frame-by-frame
    ret,frame=cap.read()
    
    #operation on frame
    
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    #Display the resulting frame
    
    cv2.imshow('frame',gray)
    if(cv2.waitKey(1)& 0xFF == ord('q')):
        cv2.imwrite('fg.jpg',frame)
        break

cap.release()
cv2.destroyAllWindows()

img=cv2.imread('fg.jpg',13)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

    
    
