# This Python file uses the following encoding: utf-8
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic


class Interface(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("interface.ui", self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Interface()
    window.show()
    sys.exit(app.exec_())

#   lien vers un exemple pour afficher une image
#   https://gist.github.com/bsdnoobz/8464000
