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
data=np.concatenate((h1,h2,h3,h4,h5,h6),axis=1)
cluster=createCluster(data)
print(cluster)

