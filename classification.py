import cv2 
import numpy as np
from sklearn.cluster import MeanShift
import matplotlib.pyplot as plt


def classifier(image,classes):
    """Retourne la classe de l'image en paramètre"""
    FeatureVector=featureCalculator(image)
    les_distances=np.zeros(1,len(classes))
    
    

    

def featureCalculator(image):
    """Calcule le vecteur caractèristique de l'image"""
    return(np.zeros(5))
    

def segmenatationMain(image):
    """"Fonction qui binarise l'image de la main
    input : image centrée sur la main 
    output : image binaire d la main """
    if np.size(image)!=(512,512):
        image=cv2.resize(image,(512,512))
    imLab=cv2.cvtColor(image,cv2.COLOR_BGR2LAB)
    ms=MeanShift(0.2)
    ms.fit(imLab[:,:,1])
    lblsAll=ms.labels_ 
    cluster_centers=ms.cluster_centers_ #calcule les centres des classes
    lbls=np.unique(lblsAll) #supprime les doublons
    k=len(lbls) #nombre de classe
    return(lblsAll,k,cluster_centers)

image=cv2.imread('7.jpg')
#cv2.namedWindow('Input')
#cv2.resizeWindow('Input',512,512)
#image=cv2.resize(image,(512,512))
#cv2.imshow("Input",image)
#imseg,k,centers=segmenatationMain(image)
#cv2.imshow('Input',imseg)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

plt.imread('7.jpg')
imseg,k,centers=segmenatationMain(image)
plt.figure();
plt.imshow(imseg)
plt.show()