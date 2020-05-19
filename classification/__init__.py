import cv2 
import numpy as np
from sklearn.cluster import MeanShift,KMeans
import pywt


def findcluster(features_vector,cluster_centers):
    data=cluster_centers-features_vector
    distances=np.linalg.norm(data,ord=None,axis=1)
    indice=np.argmin(distances)
    return(indice)

def createCluster(base):
     """Renvoie les clusters de la base
     base n vecteur de m features """
     nbcluster=7
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
    #k=ms.predict(np.reshape([140,140],(1,-1)))
    image_seg=np.where(lblsAll==k,1,0)      
    image_seg=np.reshape(image_seg,taille)
    return(image_seg)
    #return(np.reshape(lblsAll,taille))

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

def createFeatureVector(imseg):
    """Return feature vector of image""" 
    #imseg=segmenatationMain(image)
    h=hog(imseg.astype(np.uint8))
    #s=surface(imseg)
    #o=orientation(imseg)
    #cw=wavelet(image)
    #add more feature if needed
    #fv=np.concatenate((h[100:-1],[[s]],[[np.size(image[:,:,0])]],[[o]]),axis=0)
    #fv=np.concatenate(([[s]],[[np.size(image[:,:,0])]],[[o]]),axis=0)
    #return(fv)
    return(h)
    
def wavelet(image):
    taille=(64,64)
    if np.shape(image)!=taille:
        image=cv2.resize(image,taille)
    imLab=cv2.cvtColor(image,cv2.COLOR_BGR2LAB)
    #print(np.shape(imLab))
    coeffs=pywt.downcoef('d', np.reshape(imLab[:,:,0],taille[0]*taille[1]),'Haar')
    return(np.atleast_2d(coeffs).T)
    

def initcluster():
    img1=cv2.imread('1.jpg')
    img2=cv2.imread('2.jpg')
    img3=cv2.imread('3.jpg')
    img4=cv2.imread('4.jpg')
    img5=cv2.imread('5.jpg')
    img6=cv2.imread('6.jpg')
    img7=cv2.imread('7.jpg')
    img8=cv2.imread('8.jpg')
    img9=cv2.imread('9.jpg')
    img10=cv2.imread('10.jpg')
    img11=cv2.imread('11.jpg')
    img12=cv2.imread('12.jpg')
    img13=cv2.imread('13.jpg')
    img14=cv2.imread('14.jpg')
    img15=cv2.imread('15.jpg')
    img16=cv2.imread('16.jpg')
    img17=cv2.imread('17.jpg')
    img18=cv2.imread('18.jpg')
    img19=cv2.imread('19.jpg')
    img20=cv2.imread('20.jpg')
    img21=cv2.imread('21.jpg')
    h1=createFeatureVector(img1)    
    h2=createFeatureVector(img2)
    h3=createFeatureVector(img3)
    h4=createFeatureVector(img4)
    h5=createFeatureVector(img5)
    h6=createFeatureVector(img6)
    h7=createFeatureVector(img7)    
    h8=createFeatureVector(img8)
    h9=createFeatureVector(img9)
    h10=createFeatureVector(img10)
    h11=createFeatureVector(img11)
    h12=createFeatureVector(img12)
    h13=createFeatureVector(img13)    
    h14=createFeatureVector(img14)
    h15=createFeatureVector(img15)
    h16=createFeatureVector(img16)
    h17=createFeatureVector(img17)
    h18=createFeatureVector(img18)
    h19=createFeatureVector(img19)    
    h20=createFeatureVector(img20)
    h21=createFeatureVector(img21)
    data=np.concatenate((h1.T, h4.T,h7.T,h10.T,h13.T,h16.T,h19.T,h2.T, h5.T,h8.T,h11.T,h14.T,h17.T,h20.T,h3.T, h6.T,h9.T,h12.T,h15.T,h18.T,h21.T),axis=0)
    cluster1=createCluster(data)
    cluster2=np.zeros(np.shape(cluster1))
    cluster2[0]=cluster1[findcluster(h1.T,cluster1)]
    cluster2[1]=cluster1[findcluster(h4.T,cluster1)]
    cluster2[2]=cluster1[findcluster(h7.T,cluster1)]
    cluster2[3]=cluster1[findcluster(h10.T,cluster1)]
    cluster2[4]=cluster1[findcluster(h13.T,cluster1)]
    cluster2[5]=cluster1[findcluster(h16.T,cluster1)]
    cluster2[6]=cluster1[findcluster(h19.T,cluster1)]
    return(cluster2)

def find_skeleton2(img):
    skeleton = np.zeros(img.shape,np.uint8)
    eroded = np.zeros(img.shape,np.uint8)
    temp = np.zeros(img.shape,np.uint8)

    #_,thresh = cv2.threshold(img,127,255,0)

    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))
    thresh=img
    iters = 0
    while(True):
        cv2.erode(thresh, kernel, eroded)
        cv2.dilate(eroded, kernel, temp)
        cv2.subtract(thresh, temp, temp)
        cv2.bitwise_or(skeleton, temp, skeleton)
        thresh = eroded.copy()

        iters += 1
        if cv2.countNonZero(thresh) == 0:
            return (skeleton,iters)

def moment(image):
    return(cv2.moments(image))
    
def orientation(imseg):
    mms=moment(imseg.astype(np.uint8))
    x,y=mms['m10']/mms['m00'],mms['m01']/mms['m00']
    a=mms['m20']/mms['m00']-x**2
    b=2*(mms['m11']/mms['m00']-x*y)
    c=mms['m02']/mms['m00']-y**2
    return(0.5*np.arctan(b/(a-c)))