# -*- coding: utf-8 -*-
"""
Created on Wed May  6 11:45:34 2020

@author: Arthu
"""

import cv2
import os
import numpy as np
from pretraitement import pretraitement
from sklearn.metrics import *

for k in range(1,22):
    p, q, r, s = 60, 10, 60, 10
    frame = cv2.imread("./Base d'images test/{}.jpg".format(k))
    frame = cv2.resize(frame,(400,225))
    main = pretraitement(frame, p, q, r, s)
    path = './Resultats'
    cv2.imwrite(os.path.join(path , 'Image_main{}.jpg'.format(k)), main[0])
    
fond = cv2.imread("./Base d'images test/1.jpg")
image = cv2.imread("./Base d'images test/4.jpg")
soustraction = cv2.subtract(fond,image)
#soustraction[np.where((soustraction > [0,0,0]).all(axis = 2))] = [255,255,255]
#cv2.imshow('difference', soustraction)
#cv2.waitKey(5000)

for k in range(1,13):
    frame = cv2.imread("./Resultats/Image_main{}.jpg".format(k))
    frame=cv2.resize(frame,(60,60))
    frame=np.reshape(frame[:,:],3600*3)
    verite = cv2.imread("./Verite terrain/{}.jpg".format(k))
    verite=cv2.resize(verite,(60,60))
    verite=np.reshape(verite[:,:],3600*3)
    rand = adjusted_rand_score(frame, verite)
    jaccard = jaccard_score(frame, verite, None, 1, 'weighted', None)
    print("Rand = ", rand)
    print("Jaccard = ", jaccard)
    #cv2.imshow('Jaccard', jaccard)
    #cv2.waitKey(2000)
    print("-------------------")
cv2.destroyAllWindows()