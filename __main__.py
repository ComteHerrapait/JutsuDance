# This Python file uses the following encoding: utf-8

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
import sys

from acquisition import *


class Interface(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("interface.ui", self)

        #timer responsable du rafraichissement de l'interface
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(30)

    def update(self):
        """ mets à jour l'affichage sur l'interface"""
        #affiche le flux de la caméra
        frame = acq("RGB")
        image = QtGui.QImage(frame, frame.shape[1], frame.shape[0],
                       frame.strides[0], QtGui.QImage.Format_RGB888)
        self.label.setPixmap(QtGui.QPixmap.fromImage(image))

if __name__ == "__main__":
    """Fonction MAIN """

    app = QtWidgets.QApplication(sys.argv)
    window = Interface()
    window.show()
    sys.exit(app.exec_())




    #   lien vers un exemple pour afficher une image
    #   https://gist.github.com/bsdnoobz/8464000
