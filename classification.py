import cv2 
import numpy as np
from sklearn.cluster import MeanShift
import matplotlib.pyplot as plt


     

def segmenatationMain(image):
    """"Fonction qui binarise l'image de la main
    input : image centrée sur la main 
    output : image binaire d la main """
    taille=(64,64)
    if np.size(image)!=taille:
        image=cv2.resize(image,taille)
    imLab=cv2.cvtColor(image,cv2.COLOR_BGR2LAB)
    plana=np.reshape(imLab[:,:,1],taille[1]*taille[0])
    planb=np.reshape(imLab[:,:,2],taille[1]*taille[0])
    data=np.concatenate((np.atleast_2d(plana).T,np.atleast_2d(planb).T),axis=1)  
    bdw=10
    ms=MeanShift(bdw)
    ms.fit(data)
    lblsAll=ms.labels_ 
    #cluster_centers=ms.cluster_centers_ #calcule les centres des classes
    #lbls=np.unique(lblsAll) #supprime les doublons
    #k=len(lbls) #nombre de classe
    image_seg=np.reshape(lblsAll,taille)
    return(image_seg)

image=cv2.imread('7.jpg')
# cv2.namedWindow('Input')
# cv2.resizeWindow('Input',512,512)
# image=cv2.resize(image,(512,512))
# cv2.imshow("Input",image)
# imseg=segmenatationMain(image)
# cv2.imshow('Input',imseg)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

imseg=segmenatationMain(image)
plt.figure();
plt.imshow(imseg)
plt.show()