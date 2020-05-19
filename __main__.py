# This Python file uses the following encoding: utf-8

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
import sys

from classification import createFeatureVector, createCluster, findcluster, initcluster
from pretraitement import pretraitement
from hog import *

class Interface(QtWidgets.QMainWindow):
    webcam = cv2.VideoCapture(0,cv2.CAP_ANY)
    cameraIndex = 0
    mainX = 60
    mainY = 60
    preview = webcam.read()[1]
    centers = initcluster()
    imagesSignes = []
    
    def __init__(self):
        """constructeur"""
        print("attributs initialisés")
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("interface.ui", self)
        
        if not self.webcam.isOpened(): raise IOError("No camera attached")
        
        #slots connection
        self.buttonCamera.released.connect(self.cycleinput)
        self.buttonSave.released.connect(self.save)

        #timer responsable du rafraichissement de l'interface
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(0)
        
        #taille de la capture camera
        self.webcam.set(4,400) # 4 : format de l'image en hauteur
        self.webcam.set(3,640) # 3 : format de l'image en largeur
        
        #stockage de la base d'image dans un vecteur
        for i in range(1,22,3):
            path = 'base images crop/'+str(i)+'.jpg'
            frame = cv2.cvtColor(
                cv2.imread(path),
                cv2.COLOR_BGR2RGB)
            self.imagesSignes.append(frame)
            
        print("initialisation terminée")


    def display(self,image1,image2, image3):
        """affiche une image dans le label au centre de l'interface"""   
        self.label.setPixmap(
            QtGui.QPixmap.fromImage(image1).scaled(640,400,QtCore.Qt.KeepAspectRatio)
            )
        self.label2.setPixmap(
            QtGui.QPixmap.fromImage(image2).scaled(100,100,QtCore.Qt.KeepAspectRatio)
            )
        self.label3.setPixmap(
            QtGui.QPixmap.fromImage(image3).scaled(100,100,QtCore.Qt.KeepAspectRatio)
            )

    def update(self):
        """ mets à jour l'affichage sur l'interface"""      
        check, frameBGR = self.webcam.read()  
        
            #vérifie que l'image est bien capturée
        if not frameBGR is None and len(frameBGR) != 0: 
            frame = cv2.cvtColor(frameBGR, cv2.COLOR_BGR2RGB)
            self.preview = frame.copy()
            
                #redimensionne l'image autour de la main (Partie Arthur)
            frameTemp, self.mainY, self.mainX = pretraitement(frame, 
                                                              self.mainY, 200, 
                                                              self.mainX, 200)
            frameCrop =    frameTemp.copy()#necessaire pour eviter des problèmes de conversion
                
                #classification (Partie Jean-Baptiste)
            featureVector = createFeatureVector(frameCrop)
            indice  =       findcluster(featureVector.T, self.centers)
            frameClass =    self.imagesSignes[indice]
            
                #Affiche sur l'interface
            image =      QtGui.QImage(frame,frame.shape[1],frame.shape[0],frame.strides[0],QtGui.QImage.Format_RGB888)#adapte le format à l'affichage
            imageCrop =  QtGui.QImage(frameCrop ,frameCrop.shape[1],frameCrop.shape[0],frameCrop.strides[0], QtGui.QImage.Format_RGB888)
            imageClass = QtGui.QImage(frameClass ,frameClass.shape[1],frameClass.shape[0],frameClass.strides[0], QtGui.QImage.Format_RGB888)
            self.display(image, imageCrop, imageClass)
            
    def changeInput(self,cameraIndex):
        """change la camera utilisée"""
        newCam = cv2.VideoCapture(cameraIndex,cv2.CAP_ANY)
        if newCam is None or not newCam.isOpened():
            print("Cannot open webcam "+str(cameraIndex))
            del newCam
            return False
        else:
            self.webcam.release()
            self.webcam = newCam
            return True
        
    def cycleinput(self):
        """cycle les cameras"""
            #essaie d'utiliser la camera suivante
        if self.changeInput(self.cameraIndex + 1):
            self.cameraIndex += 1
            
            #sinon, repasse à la première
        elif self.changeInput(0):
            self.cameraIndex = 0    
        print("utilise maintenant la camera : ", self.cameraIndex)

    def save(self):
        imgBGR=cv2.cvtColor(self.preview, cv2.COLOR_RGB2BGR)
        cv2.imwrite(filename=("capture.jpg"), img=imgBGR)
        print("image sauvegardée dans capture.jpg")

    def closeEvent(self,event):
        self.webcam.release()
        event.accept()
        
if __name__ == "__main__":
    """Fonction MAIN """
    
    print("début de l'initialisation")
    app = QtWidgets.QApplication(sys.argv)
    window = Interface()
    window.show()
    print("arret avec code ",app.exec_())
    I = window.imagesSignes
    sys.exit()

