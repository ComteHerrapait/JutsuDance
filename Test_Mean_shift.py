# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 17:03:52 2020

@author: Arthu
"""

import numpy as np 
import cv2 
   
  
# read video 
cap = cv2.VideoCapture(0) 
   
# retrieve the very first  
# frame from the video
fond = cv2.imread("./fond.jpg")
_, frame = cap.read()
#frame = cv2.subtract(fond,frame)

   
# set the region for the 
# tracking window p, q, r, s 
# put values according to yourself 
p, q, r, s = 150, 150, 460, 100
track_window = (r, p, s, q) 
   
      
# create the region of interest 
r_o_i = frame[p:p + q, r:r + s] 
  
# converting BGR to HSV format 
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
   
# apply mask on the HSV frame 
mask = cv2.inRange(hsv, np.array((0., 61., 33.)), np.array((180., 255., 255.))) 
  
# get histogram for hsv channel 
roi = cv2.calcHist([hsv], [0], mask, [180], [0, 180]) 
  
# normalize the retrieved values 
cv2.normalize(roi, roi, 0, 255, cv2.NORM_MINMAX) 
   
# termination criteria, either 15  
# iteration or by at least 2 pt 
termination = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 15, 2 ) 
   
while(True): 
    _, frame = cap.read() 
    frame = cv2.flip(frame, 1)
    #frame = cv2.subtract(fond,frame)
   
    frame = cv2.resize(frame, (1280, 720), fx = 0, fy = 0, interpolation = cv2.INTER_CUBIC) 
   
    # convert BGR to HSV format 
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    cv2.imshow('hsv', hsv)
      
    bp = cv2.calcBackProject([hsv], [0], roi, [0, 180], 1) 
   
    # applying meanshift to get the new region 
    _, track_window = cv2.meanShift(bp, track_window, termination)
    #ret, track_window = cv2.CamShift(bp, track_window, termination) 
   
    # Draw track window on the frame 
    x, y, w, h = track_window 
    img2 = cv2.rectangle(frame, (x, y), (x + w*2, y + h*2), 255, 2) 
    #pts = cv2.boxPoints(ret)
    #pts = np.int0(pts)
    #img2 = cv2.polylines(frame,[pts],True, 255,2)
      
    # show results 
    cv2.imshow('tracker', img2)
   
    k = cv2.waitKey(1) & 0xff
    if k == ord('q'):
        img_meanshift = cv2.imwrite(filename='saved_img-final_MS.jpg', img=img2)
        break
          
# release cap object 
cap.release() 
  
# destroy all opened windows 
cv2.destroyAllWindows() 
