import cv2
import os

class camera():
    """
    class in charge of interaction with th webcam
    """
    ### Attributes ###
    webcam = cv2.VideoCapture(0)


    def __init__(self,cameraIndex=0):
        """constructor"""
        #CAP_ANY correspond à la méthode de capture de l'image (backend)
        webcam = cv2.VideoCapture(cameraIndex,cv2.CAP_DSHOW)


    def acq(self,space, height=480,width=640):
        """
        3 arguments : space , height, width
        - space : 4 formats possibles : 'HSV','LAB','RGB' et pas défaut BGR
        - height : hauteur en pixel de l'image à acquérir, par défaut height=480
        - width : largeur en pixel de l'image à acquérir, par défaut width=640

        Retourne la matrice définissant l'image dans l'espace couleur et les dimensions indiqués
        """

        if self.webcam.isOpened(): #on vérifie que la prise d'image a bien fonctionné
            self.webcam.set(4,height) # 4 : format de l'image en hauteur
            self.webcam.set(3,width) # 3 : format de l'image en largeur
            check, img = self.webcam.read()

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
        else :
            raise IOError("Cannot open webcam")


    def save(self,name,image):
        """
        2 arguments : name, image
        -name : nom de l'image (format de sortie : name.jpg)'
        -image : image à enregistrer

        Ne renvoie rien
        """
        imgBGR=cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        cv2.imwrite(filename=(name+'.jpg'), img=imgBGR)

    def __del__(self):
        """desructor"""
        self.webcam.release() # On stop l'utilisation de la caméra

