# -*- coding: utf-8 -*-
"""
Created on Sun May 17 14:16:11 2020

@author: jbapt
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt 
from classification import createCluster,findcluster
from HOGtest import hog

img1=cv2.cvtColor(cv2.imread('1.jpg'), cv2.COLOR_BGR2HSV)
img2=cv2.cvtColor(cv2.imread('2.jpg'), cv2.COLOR_BGR2HSV)
img3=cv2.cvtColor(cv2.imread('3.jpg'), cv2.COLOR_BGR2HSV)
img4=cv2.cvtColor(cv2.imread('4.jpg'), cv2.COLOR_BGR2HSV)
img5=cv2.cvtColor(cv2.imread('5.jpg'), cv2.COLOR_BGR2HSV)
img6=cv2.cvtColor(cv2.imread('6.jpg'), cv2.COLOR_BGR2HSV)

h1=hog(img1,1)
h2=hog(img2,1)
h3=hog(img3,1)
h4=hog(img4,1)
h5=hog(img5,1)
h6=hog(img6,1)
data=np.concatenate((h1.T,h2.T,h4.T,h5.T),axis=0)
print(np.shape(data))
cluster=createCluster(data)
print('cluster : ')
print(np.shape(cluster))
i=findcluster(h3.T,cluster)
print(i)
j=findcluster(h3.T, cluster)
print(j)
