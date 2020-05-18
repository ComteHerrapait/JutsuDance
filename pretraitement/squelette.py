# -*- coding: utf-8 -*-
"""
Created on Mon May 18 18:57:40 2020

@author: Arthu
"""


# Import the necessary libraries
import cv2
import numpy as np

def find_skeleton2(img):
    skeleton = np.zeros(img.shape,np.uint8)
    eroded = np.zeros(img.shape,np.uint8)
    temp = np.zeros(img.shape,np.uint8)

    _,thresh = cv2.threshold(img,127,255,0)

    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))

    iters = 0
    while(True):
        cv2.erode(thresh, kernel, eroded)
        cv2.dilate(eroded, kernel, temp)
        cv2.subtract(thresh, temp, temp)
        cv2.bitwise_or(skeleton, temp, skeleton)
        thresh = eroded.copy()

        iters += 1
        if cv2.countNonZero(thresh) == 0:
            return (skeleton,iters)