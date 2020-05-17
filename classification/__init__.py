import cv2 
import numpy as np
from sklearn.cluster import MeanShift,KMeans
import matplotlib.pyplot as plt


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

def surface(im_seg):
    """Calcul de la surface de la main"""
    return(np.sum(np.sum(im_seg))/256)
    
    
    

# image=cv2.imread('1.jpg')
# imseg=segmenatationMain(image)
# print(surface(imseg))
# plt.figure();
# plt.imshow(imseg)
# plt.show()