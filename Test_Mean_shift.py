# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 17:03:52 2020

@author: Arthu
"""

import numpy as np 
import cv2
import matplotlib.pyplot as plt

  
# read video 
cap = cv2.VideoCapture(0) 
# retrieve the very first  
# frame from the video
#fond = cv2.imread("./fond.jpg")
_, frame = cap.read()
#frame = cv2.subtract(fond,frame)
main = cv2.imread("./Image_main.jpg")
main_hsv = cv2.cvtColor(main, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(main_hsv, np.array((0., 60.,32.)), np.array((180.,255.,255.)))
roi1 = cv2.calcHist([main_hsv], [0], mask, [180], [0, 180])
roi2 = cv2.calcHist([main_hsv], [1], mask, [180], [0, 180])
roi3 = cv2.calcHist([main_hsv], [2], mask, [180], [0, 180])
cv2.imshow('main', main_hsv)
plt.hist(roi1)
plt.show()
plt.hist(roi2)
plt.show()
plt.hist(roi3)
plt.show()

   
# set the region for the 
# tracking window p, q, r, s 
# put values according to yourself 
p, q, r, s = 150, 150, 400, 120
track_window = (r, p, s, q) 
   
      
# create the region of interest 
r_o_i = frame[p:p + q, r:r + s] 
  
# converting BGR to HSV format 
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
   
# apply mask on the HSV frame 
mask = cv2.inRange(hsv, np.array((0., 60.,32.)), np.array((180.,255.,255.))) 
  
# get histogram for hsv channel 
roi = cv2.calcHist([hsv], [1], mask, [180], [0, 180])
#plt.hist(roi)
  
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
      
    bp = cv2.calcBackProject([hsv], [1], roi, [0, 180], 1) 
   
    # applying meanshift to get the new region 
    #_, track_window = cv2.meanShift(bp, track_window, termination)
    ret, track_window = cv2.CamShift(bp, track_window, termination) 
   
    # Draw track window on the frame 
    #x, y, w, h = track_window 
    #img2 = cv2.rectangle(frame, (x, y), (x + w*2, y + h*2), 255, 2) 
    pts = cv2.boxPoints(ret)
    pts = np.int0(pts)
    img2 = cv2.polylines(frame,[pts],True, 255,2)
      
    # show results 
    cv2.imshow('tracker', img2)
   
    k = cv2.waitKey(1) & 0xff
    if k == ord('q'):
        img_meanshift = cv2.imwrite(filename='saved_img-final_MS.jpg', img=img2)
        break
    if k == ord('m'):
        x = min(pts[0][0],pts[1][0],pts[2][0],pts[3][0])
        y = min(pts[0][1],pts[1][1],pts[2][1],pts[3][1])
        w = max(pts[0][0],pts[1][0],pts[2][0],pts[3][0])
        h = max(pts[0][1],pts[1][1],pts[2][1],pts[3][1])
        img3 = frame[y:h,x:w]
        img_main = cv2.imwrite(filename='Image_main.jpg', img=img3)
        break
       
# release cap object 
cap.release() 
  
# destroy all opened windows 
cv2.destroyAllWindows() 
