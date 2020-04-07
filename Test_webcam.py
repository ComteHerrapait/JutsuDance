# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 14:24:16 2020

@author: Arthu
"""

import cv2
import numpy as np
import time

key = cv2. waitKey(1)
webcam = cv2.VideoCapture(0)
fond = cv2.imread("./fond.jpg")
while True:
    try:
        check, frame = webcam.read()
        print(check) #prints true as long as the webcam is running
        print(frame) #prints matrix values of each framecd
        frame = cv2.flip(frame, 1)
        image_sans_fond = cv2.subtract(fond,frame)
        gray = cv2.cvtColor(image_sans_fond, cv2.COLOR_BGR2GRAY)
        #cv2.imshow("frame", frame)
        #cv2.imshow("fond", fond)
        cv2.imshow("Capturing", gray)
        key = cv2.waitKey(1)
        if key == ord('s'): 
            cv2.imwrite(filename='saved_img.jpg', img=frame)
            webcam.release()
            img_new = cv2.imread('saved_img.jpg', cv2.IMREAD_GRAYSCALE)
            img_new = cv2.imshow("Captured Image", img_new)
            cv2.waitKey(1650)
            cv2.destroyAllWindows()
            print("Processing image...")
            img_ = cv2.imread('saved_img.jpg', cv2.IMREAD_ANYCOLOR)
            print("Converting RGB image to grayscale...")
            gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
            print("Converted RGB image to grayscale...")
            print("Top-Hat...")
            kernel = np.ones((20,20),np.uint8)
            grad = cv2.morphologyEx(frame, cv2.MORPH_GRADIENT, kernel)
            canny = cv2.Canny(gray, 100, 200)
            print("Top-Hat...")
            #cv2.imshow("Captured Image", tophat)
            # Wait for 5 seconds
            #time.sleep(2)
            print("Resizing image to 28x28 scale...")
            #img_ = cv2.resize(tophat,(28,28))
            print("Resized...")
            img_grad = cv2.imwrite(filename='saved_img-final_grad.jpg', img=grad)
            img_canny = cv2.imwrite(filename='saved_img-final_canny.jpg', img=canny)
            print("Image saved!")
            break
        elif key == ord('q'):
            print("Turning off camera.")
            webcam.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()
            break
        
    except(KeyboardInterrupt):
        print("Turning off camera.")
        webcam.release()
        print("Camera off.")
        print("Program ended.")
        cv2.destroyAllWindows()
        break
    
