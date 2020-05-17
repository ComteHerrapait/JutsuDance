# -*- coding: utf-8 -*-
"""
Created on Sun May 17 14:16:11 2020

@author: jbapt
"""
import cv2
import numpy as np
import classification as cl


img1=cv2.cvtColor(cv2.imread('1.jpg'), cv2.COLOR_BGR2LAB)
img2=cv2.cvtColor(cv2.imread('2.jpg'), cv2.COLOR_BGR2LAB)
img3=cv2.cvtColor(cv2.imread('3.jpg'), cv2.COLOR_BGR2LAB)
img4=cv2.cvtColor(cv2.imread('4.jpg'), cv2.COLOR_BGR2LAB)
img5=cv2.cvtColor(cv2.imread('5.jpg'), cv2.COLOR_BGR2LAB)
img6=cv2.cvtColor(cv2.imread('6.jpg'), cv2.COLOR_BGR2LAB)


h1=cl.createFeatureVector(img1)    
h2=cl.createFeatureVector(img2)
h3=cl.createFeatureVector(img3)
h4=cl.createFeatureVector(img4)
h5=cl.createFeatureVector(img5)
h6=cl.createFeatureVector(img6)



data=np.concatenate((h1.T,h2.T,h4.T,h5.T),axis=0)

cluster=cl.createCluster(data)
print(cl.findcluster(h1.T, cluster))
print(cl.findcluster(h2.T, cluster))
print(cl.findcluster(h3.T, cluster))
print(cl.findcluster(h4.T, cluster))
print(cl.findcluster(h5.T, cluster))
print(cl.findcluster(h6.T, cluster))
