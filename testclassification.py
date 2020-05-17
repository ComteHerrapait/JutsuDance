# -*- coding: utf-8 -*-
"""
Created on Sun May 17 14:16:11 2020

@author: jbapt
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt 
import classification as cl
import HOGtest as HOG

img1=cv2.cvtColor(cv2.imread('1.jpg'), cv2.COLOR_BGR2LAB)
img2=cv2.cvtColor(cv2.imread('2.jpg'), cv2.COLOR_BGR2LAB)
img3=cv2.cvtColor(cv2.imread('3.jpg'), cv2.COLOR_BGR2LAB)
img4=cv2.cvtColor(cv2.imread('4.jpg'), cv2.COLOR_BGR2LAB)
img5=cv2.cvtColor(cv2.imread('5.jpg'), cv2.COLOR_BGR2LAB)
img6=cv2.cvtColor(cv2.imread('6.jpg'), cv2.COLOR_BGR2LAB)


img1=cl.segmenatationMain(img1)
img2=cl.segmenatationMain(img2)
img3=cl.segmenatationMain(img3)
img4=cl.segmenatationMain(img4)
img5=cl.segmenatationMain(img5)
img6=cl.segmenatationMain(img6)

h1=HOG.hog_BW(img1.astype(np.uint8))    
h2=HOG.hog_BW(img2.astype(np.uint8))
h3=HOG.hog_BW(img3.astype(np.uint8))
h4=HOG.hog_BW(img4.astype(np.uint8))
h5=HOG.hog_BW(img5.astype(np.uint8))
h6=HOG.hog_BW(img6.astype(np.uint8))




data=np.concatenate((h1.T,h2.T,h4.T,h5.T),axis=0)

cluster=cl.createCluster(data)
print(cl.findcluster(h1.T, cluster))
print(cl.findcluster(h2.T, cluster))
print(cl.findcluster(h3.T, cluster))
print(cl.findcluster(h4.T, cluster))
print(cl.findcluster(h5.T, cluster))
print(cl.findcluster(h6.T, cluster))
