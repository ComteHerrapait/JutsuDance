# -*- coding: utf-8 -*-
"""
Created on Thu May 21 12:59:05 2020

@author: ComteHerappait
"""
import sys
import cv2
import numpy as np
from matplotlib import pyplot as mpl

from classification import findcluster, initcluster, segmenatationMain, hog
from pretraitement import pretraitement

def init():
        #initialisation des clusters de classification
    centers = initcluster()
    print("-> cluters initialisés")
        #stockage des images à tester dans un vecteur
    imagesTest = []
    print("-> chargement des images : >",end="")
    for i in range(1,22):
        path = "Base d'images test/"+str(i)+".jpg"
        frame = cv2.cvtColor( cv2.imread(path) , cv2.COLOR_BGR2RGB )
        imagesTest.append(frame)
        print("#",end="")
    print("<")
    return centers, imagesTest
    
def test(centers, images, taille = 100):
        #chaine de traitement   
    resultats = []
    print("-> traitement des images : >",end="")
    for frame in images:       
            #redimensionne l'image autour de la main (Partie Arthur)
        frameTemp, mainY, mainX = pretraitement(frame,60, taille,60, taille)
        frameCrop =    frameTemp.copy()     #necessaire pour eviter des problèmes de conversion
            #segmentation (Partie Jean-Baptiste)
        frameSeg =      segmenatationMain(frameCrop)
            #classification (Partie Jean-Baptiste)
        featureVector = hog(frameSeg.astype(np.uint8))
        indice  =       findcluster(featureVector.T, centers)
        resultats.append(indice)
        print("#",end="")
    print("<")
    return resultats
    
def displayUnique(res) :
        #affichage des resultats
    print("résultats des traitements :")
    for i in range(1,22):
        reality = (i+2)//3
        guess   = res[i-1]
        print(i,res[i-1],reality==guess, sep="\t")
        
def evaluationUnique(taille = 100):
    centers, images = init()
    results = test(centers, images, taille)
    displayUnique(results)
    
def evaluationMultiple(n=10,taille = 100):
    resultatMultiple = np.zeros((7,7))
    for boucle in range(1,n+1):
        print("test",boucle,"/",n," :")
        centers, images = init()
        results = test(centers, images, 100)
        for i in range(1,22):
            reality = (i+2)//3 - 1
            guess   = results[i-1]
            resultatMultiple[guess,reality] += 1
                
    return resultatMultiple
            
        
def tauxReussite(res):
    reussites = [res[i,i] for i in range(7)]
    print("taux de réussite : ",100 * sum(reussites)/np.sum(res),"%")
        
if __name__ == "__main__" :
    TAILLE = 10
    NOMBRE_TESTS = 25
    
    print('###\tbegin\t###')
    r = evaluationMultiple(NOMBRE_TESTS,TAILLE)
    print("#*#*#*#*#*#*#*#*#*#*#*#*#*#*#")
    print("lignes : nombres devinés",
          "\ncolonnes : nombres rééls")
    print(r)
    tauxReussite(r)
    print("sur", NOMBRE_TESTS, "tests, avec taille = ", TAILLE)
    print('###\tend\t###')
    
    
    
    
    
    
    
    