import cv2 
import numpy as np
from scipy.spatial import distance

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
    imseg=cv2.pyrMeanShiftFiltering(imLab,30,20)
    return(imseg)

image=cv2.imread('7.jpg')
cv2.namedWindow('Input')
cv2.resizeWindow('Input',512,512)
#image=cv2.resize(image,(512,512))
#cv2.imshow("Input",image)
imsegement=segmenatationMain(image)
cv2.imshow('Input',imsegement)

cv2.waitKey(0)
cv2.destroyAllWindows()
