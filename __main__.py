# This Python file uses the following encoding: utf-8

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
import sys

from acquisition import *


class Interface(QtWidgets.QMainWindow):
    camera = Camera()
    CameraIndex = 0

    def __init__(self):
        """constrcteur"""
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("interface.ui", self)

        #slots connection
        self.buttonSave.released.connect(self.savePreview)
        self.buttonPlus.released.connect(self.plus)
        self.buttonMinus.released.connect(self.minus)

        #timer responsable du rafraichissement de l'interface
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(30)

    def display(self,image):
        """affiche une image dans le label au centre de l'interface"""
        image = QtGui.QImage(image, image.shape[1], image.shape[0],
                       image.strides[0], QtGui.QImage.Format_RGB888)
        self.label.setPixmap(QtGui.QPixmap.fromImage(image))

    def update(self):
        """ mets à jour l'affichage sur l'interface"""
        #affiche le flux de la caméra
        frame = self.camera.acq("RGB")
        self.display(frame)

    def __del__(self):
        """destructeur"""
        cv2.destroyAllWindows()

    def plus(self):
        """camera suivante"""
        if self.camera.changeInput(self.CameraIndex + 1):
            self.CameraIndex +=1
            self.labelCamera.setText(str(self.CameraIndex))

    def minus(self):
        """camera précédente"""
        if self.camera.changeInput(self.CameraIndex - 1):
            self.CameraIndex -=1
            self.labelCamera.setText(str(self.CameraIndex))

    def savePreview(self):
        self.camera.save("test",self.camera.acq("RGB"))

if __name__ == "__main__":
    """Fonction MAIN """

    app = QtWidgets.QApplication(sys.argv)
    window = Interface()
    window.show()
    sys.exit(app.exec_())



    #   lien vers un exemple pour afficher une image
    #   https://gist.github.com/bsdnoobz/8464000
