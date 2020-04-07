# This Python file uses the following encoding: utf-8

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
import cv2
import sys

class Interface(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("interface.ui", self)

        self.init_webcam()

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_camera)
        self.timer.start(30)


    def init_webcam(self):
        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 480) #WIDTH
        self.capture.set(4, 480) #HEIGHT

    def update_camera(self):
        _, frame = self.capture.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.flip(frame, 1)
        image = QtGui.QImage(frame, frame.shape[1], frame.shape[0],
                       frame.strides[0], QtGui.QImage.Format_RGB888)
        self.label.setPixmap(QtGui.QPixmap.fromImage(image))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Interface()
    window.show()
    sys.exit(app.exec_())

#   lien vers un exemple pour afficher une image
#   https://gist.github.com/bsdnoobz/8464000
