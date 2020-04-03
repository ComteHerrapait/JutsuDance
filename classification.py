import cv2 as opcv
import numpy as np
from scipy.spatial import distance

def classifier(image,classes):
    """Retourne la classe de l'image en paramètre"""
    FeatureVector=featureCalculator(image)
    les_distances=np.zeros(1,len(classes))
    
    

    

def featureCalculator(image):
    """Calcule le vecteur caractèristique de l'image"""
    return(np.zeros(5))
    
