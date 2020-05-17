import cv2
import numpy as np
import matplotlib.pyplot as plt 
from classification import createCluster

def hog(img,canal=1,SizeWind=16) :
    """

    3 arguments : img, canal, SizeWind
    - img : l'image prétraité que l'on souhaite étudiée
    - canal : numéro du canal sur lequel on réalise le HOG (ex : 2 pour l'espace HSV determine le diagramme sur le canal S')
        par défaut : canal=1
    - SizeWind : taille de la fenêtre d'étude (pas de l'image)
        par défaut : SizeWind=16

    Renvoie le HOG du canal souhaité sur une image redimensionnée

    """

    img=cv2.resize(img,(64,64)) #on redimensionne l'image pour


    winSize = (SizeWind,SizeWind)
    blockSize = (16,16)
    blockStride = (16,16)
    cellSize = (16,16)
    nbins = 9

    hog = cv2.HOGDescriptor(winSize,blockSize,blockStride,cellSize,nbins)

    return hog.compute(img[:,:,canal])


