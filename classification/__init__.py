import cv2 
import numpy as np
from sklearn.cluster import MeanShift,KMeans



def findcluster(features_vector,cluster_centers):
    data=cluster_centers-features_vector
    distances=np.linalg.norm(data,ord=1,axis=1)
    indice=np.argmin(distances)
    return(indice)

def createCluster(base):
     """Renvoie les clusters de la base
     base n vecteur de m features """
     nbcluster=2
     kmeans=KMeans(nbcluster).fit(base)
     return(kmeans.cluster_centers_)
        
def segmenatationMain(image):
    """Fonction qui binarise l'image de la main
    input : image centrée sur la main 
    output : image binaire d la main """
    taille=(64,64)
    if np.shape(image)!=taille:
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
    image_seg=np.where(lblsAll==k,1,0)      
    image_seg=np.reshape(image_seg,taille)
    return(image_seg)

def surface(im_seg):
    """Calcul de la surface de la main"""
    return(np.sum(np.sum(im_seg)))
    
    
def hog(img,SizeWind=16) :
    """
    3 arguments : img, canal, SizeWind
    - img : l'image prétraité que l'on souhaite étudiée
    - canal : numéro du canal sur lequel on réalise le HOG (ex : 2 pour l'espace HSV determine le diagramme sur le canal S')
        par défaut : canal=1
    - SizeWind : taille de la fenêtre d'étude (pas de l'image)
        par défaut : SizeWind=16
    Renvoie le HOG du canal souhaité sur une image redimensionnée"""
    img=cv2.resize(img,(64,64)) #on redimensionne l'image pour
    winSize = (SizeWind,SizeWind)
    blockSize = (16,16)
    blockStride = (16,16)
    cellSize = (16,16)
    nbins = 9
    hog = cv2.HOGDescriptor(winSize,blockSize,blockStride,cellSize,nbins)
    return hog.compute(img)

def createFeatureVector(image):
    """Return feature vector of image"""
    imseg=segmenatationMain(image)
    h=hog(imseg.astype(np.uint8))
    #s=surface(imseg)
    #add more feature if needed
    #return(np.concatenate((h,[[s]]),axis=0))
    return(h)
    
