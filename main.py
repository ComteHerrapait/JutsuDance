# -*- coding: utf-8 -*-
"""
Created on Wed May  6 11:45:34 2020

@author: Arthu
"""

import cv2
import os
import numpy as np
from pretraitement import pretraitement

for k in range(1,13):
    frame = cv2.imread("./Base d'images/{}.jpg".format(k))
    main = pretraitement(frame)
    path = './Resultats'
    cv2.imwrite(os.path.join(path , 'Image_main{}.jpg'.format(k)), main)
    
fond = cv2.imread("./Base d'images/1.jpg")
image = cv2.imread("./Base d'images/4.jpg")
soustraction = cv2.subtract(fond,image)
soustraction[np.where((soustraction > [0,0,0]).all(axis = 2))] = [255,255,255]
cv2.imshow('difference', soustraction)
cv2.waitKey(5000)
cv2.destroyAllWindows()