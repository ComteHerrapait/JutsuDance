# This Python file uses the following encoding: utf-8

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
import sys

from acquisition import *


class Interface(QtWidgets.QMainWindow):
    camera = Camera()

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("interface.ui", self)

        #slots connection
        self.pushButton.released.connect(self.button1)
        self.spinBox.valueChanged.connect(self.changeCamera)
        #timer responsable du rafraichissement de l'interface
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(30)

    def update(self):
        """ mets à jour l'affichage sur l'interface"""
        #affiche le flux de la caméra
        frame = self.camera.acq("RGB")
        image = QtGui.QImage(frame, frame.shape[1], frame.shape[0],
                       frame.strides[0], QtGui.QImage.Format_RGB888)
        self.label.setPixmap(QtGui.QPixmap.fromImage(image))

    def __del__(self):
        cv2.destroyAllWindows()

    def button1(self):
        self.camera.save("test",self.camera.acq("BGR"))

    def changeCamera(self, index):
        #method1
        #newCam = cv2.VideoCapture(index,cv2.CAP_ANY)
        #self.camera.webcam = newCam

        #method2
        newCam = Camera(index)
        self.camera = newCam



if __name__ == "__main__":
    """Fonction MAIN """

    app = QtWidgets.QApplication(sys.argv)
    window = Interface()
    window.show()
    sys.exit(app.exec_())




    #   lien vers un exemple pour afficher une image
    #   https://gist.github.com/bsdnoobz/8464000
