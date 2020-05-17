import cv2 
import numpy as np
from sklearn.cluster import MeanShift,KMeans
import matplotlib.pyplot as plt
from sklearn.metrics.cluster import adjusted_rand_score
import time

def segmenatationMain(image):
    """Fonction qui binarise l'image de la main
    input : image centrée sur la main 
    output : image binaire d la main """
    taille=(64,64)
    if np.size(image)!=taille:
        image=cv2.resize(image,taille)
    imLab=cv2.cvtColor(image,cv2.COLOR_BGR2LAB)
    plana=np.reshape(imLab[:,:,1],taille[1]*taille[0])
    planb=np.reshape(imLab[:,:,2],taille[1]*taille[0])
    data=np.concatenate((np.atleast_2d(plana).T,np.atleast_2d(planb).T),axis=1)  
    bdw=5 #possible nécessité de set au début du programme estimate_bandwith
    ms=MeanShift(bdw,bin_seeding=True,n_jobs=-1,min_bin_freq=20)
    ms.fit(data)
    lblsAll=ms.labels_
    k=ms.predict(np.reshape([150,170],(1,-1)))
    image_seg=np.where(lblsAll==k,256,0)      
    image_seg=np.reshape(image_seg,taille)
    return(image_seg)

img=cv2.imread('3.jpg')
imgman=cv2.imread('3manuel.jpg')
imgman=cv2.resize(imgman,(64,64))
imgman=imgman[:,:,1]
a=segmenatationMain(img)

a=np.reshape(a[:,:],4096)
imgman=np.reshape(imgman[:,:],4096)
ri=adjusted_rand_score(a,imgman)

