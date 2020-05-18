# -*- coding: utf-8 -*-
"""
Created on Tue May  5 10:10:18 2020

@author: Arthu
"""

import numpy as np 
import cv2

def pretraitement(frame, p, q, r, s):    
       
    # set the region for the 
    # tracking window p, q, r, s 
    # put values according to yourself 
    track_window = (r, p, s, q) 
       
          
    # create the region of interest 
    r_o_i = frame[p:p + q, r:r + s] 
      
    # converting BGR to HSV format 
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    YCbCr = cv2.cvtColor(frame, cv2.COLOR_BGR2YCrCb)
    #cv2.imwrite(filename='image_YCbCr.jpg', img=YCbCr)
    #cv2.imwrite(filename='image_hsv.jpg', img=hsv)
       
    # apply mask on the HSV frame 
    mask_hsv = cv2.inRange(hsv, np.array((0., 60.,32.)), np.array((180.,255.,255.)))
    mask_YCbCr = cv2.inRange(YCbCr, np.array((80., 85.,135.)), np.array((255.,135.,180.))) 
      
    # get histogram for hsv channel 
    roi_hsv = cv2.calcHist([hsv], [1], mask_hsv, [180], [0, 180])
    roi_YCbCr = cv2.calcHist([YCbCr], [1], mask_YCbCr, [180], [0, 255])
    #plt.hist(roi)
      
    # normalize the retrieved values 
    cv2.normalize(roi_hsv, roi_hsv, 0, 255, cv2.NORM_MINMAX) 
    cv2.normalize(roi_YCbCr, roi_YCbCr, 0, 255, cv2.NORM_MINMAX) 
       
    # termination criteria, either 15  
    # iteration or by at least 2 pt 
    termination = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 ) 
    
    #frame = cv2.flip(frame, 1)
    #frame = cv2.resize(frame, (1280, 720), fx = 0, fy = 0, interpolation = cv2.INTER_CUBIC) 
    
    # convert BGR to HSV format 
    #hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
      
    bp_hsv = cv2.calcBackProject([hsv], [1], roi_hsv, [0, 180], 1)
    bp_YCbCr = cv2.calcBackProject([YCbCr], [1], roi_YCbCr, [0, 180], 1) 
       
    # applying meanshift to get the new region 
    _, track_window = cv2.meanShift(bp_hsv, track_window, termination)
    #_, track_window = cv2.meanShift(bp_YCbCr, track_window, termination)
       
    # Draw track window on the frame 
    x, y, w, h = track_window 
      
    # Extract hand 
    main = frame[y:y+100,x:x+100]
    return(main, y, 10, x, 10)
      
    # destroy all opened windows 
    cv2.destroyAllWindows()