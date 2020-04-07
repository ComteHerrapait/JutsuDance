import cv2
import os

def acq(space, height=480,width=640): 
    """ 
    3 arguments : space , height, width 
    - space : 4 formats possibles : 'HSV','LAB','RGB' et pas défaut BGR
    - height : hauteur en pixel de l'image à acquérir, par défaut height=480
    - width : largeur en pixel de l'image à acquérir, par défaut width=640
    
    Retourne la matrice définissant l'image dans l'espace couleur et les dimensions indiqués
    """

    #CAP_ANY correspond à la méthode de capture de l'image (backend)
    webcam = cv2.VideoCapture(0, cv2.CAP_ANY)

    if webcam.isOpened(): #on vérifie que la prise d'image a bien fonctionné

        webcam.set(4,height) # 4 : format de l'image en hauteur
        webcam.set(3,width) # 3 : format de l'image en largeur
        check, img = webcam.read()
        webcam.release() # On stop l'utilisation de la caméra

        if space=='HSV':
            imgHSV=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            return(imgHSV)
        if space=='LAB':
            imgLAB=cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
            return(imgLAB)
        if space=='RGB' :
            imgRGB=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            return(imgRGB)
        return(img) # On renvoie l'image par défaut en BGR


def save(name,image):
    """
    2 arguments : name, image
    -name : nom de l'image (format de sortie : name.jpg)'
    -image : image à enregistrer

    Ne renvoie rien
    """
    cv2.imwrite(filename=(name+'.jpg'), img=image)
