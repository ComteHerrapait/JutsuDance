# This Python file uses the following encoding: utf-8

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
import sys

from classification import *
from pretraitement import pretraitement
from hog import *

class Interface(QtWidgets.QMainWindow):
    webcam = cv2.VideoCapture(0,cv2.CAP_ANY)
    cameraIndex = 0
    
    def __init__(self):
        """constrcteur"""
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("interface.ui", self)
        
        if not self.webcam.isOpened(): raise IOError("No camera attached")
        
        #slots connection
        #self.buttonSave.released.connect(self.save)
        #self.buttonPlus.released.connect(self.plus)
        #self.buttonMinus.released.connect(self.minus)

        #timer responsable du rafraichissement de l'interface
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(30)
        
        self.webcam.set(4,400) # 4 : format de l'image en hauteur
        self.webcam.set(3,640) # 3 : format de l'image en largeur


    def display(self,image1,image2):
        """affiche une image dans le label au centre de l'interface"""   
        self.label.setPixmap(QtGui.QPixmap.fromImage(image1))
        self.label2.setPixmap(QtGui.QPixmap.fromImage(image2))

    def update(self):
        """ mets à jour l'affichage sur l'interface"""      
        #frame = self.camera.acq("RGB") #récupère l'image depuis la camera
        check, frameBGR = self.webcam.read()  
        
        if not frameBGR is None and len(frameBGR) != 0: 
               #vérifie que l'image est bien capturée
            frame =             cv2.cvtColor(frameBGR, cv2.COLOR_BGR2RGB)
            image =             QtGui.QImage(frame,frame.shape[1],frame.shape[0],frame.strides[0],QtGui.QImage.Format_RGB888)#adapte le format à l'affichage
            frameProcessed =    pretraitement(frame)
            frame2 =            frameProcessed.copy()#necessaire pour eviter des problèmes de conversion
            imageProcessed =    QtGui.QImage(frame2 ,frame2.shape[1],frame2.shape[0],frame2.strides[0], QtGui.QImage.Format_RGB888)
            
            self.display(image, imageProcessed)
            
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
        
    def plus(self):
        """camera suivante"""
        if self.changeInput(self.CameraIndex + 1):
            self.CameraIndex +=1
            self.labelCamera.setText(str(self.CameraIndex))

    def minus(self):
        """camera précédente"""
        if self.changeInput(self.CameraIndex - 1):
            self.CameraIndex -=1
            self.labelCamera.setText(str(self.CameraIndex))

    def save(self, frame):
        imgBGR=cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        cv2.imwrite(filename=("capture.jpg"), img=imgBGR)

    def closeEvent(self,event):
        self.webcam.release()
        event.accept()
        
if __name__ == "__main__":
    """Fonction MAIN """

    app = QtWidgets.QApplication(sys.argv)
    window = Interface()
    window.show()
    sys.exit(app.exec_())

