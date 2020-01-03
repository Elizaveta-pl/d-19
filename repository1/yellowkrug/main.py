from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtCore, QtGui
import random
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        self.e = random.randint(0, 300)
        self.pushButton.clicked.connect(self.fill)

    def paintEvent(self, event):  # use to draw on the canvas
        self.paint = QtGui.QPainter()
        self.paint.begin(self)
        self.paint.setRenderHint(QtGui.QPainter.Antialiasing)
        self.paint.setBrush(QtCore.Qt.white)
        self.paint.drawRect(event.rect())

    def fill(self):
        self.paint.setPen(QtCore.Qt.yellow)
        self.paint.setBrush(QtCore.Qt.yellow)
        self.paint.drawEllipse(QtCore.QRect(self.e, self.e, self.e, self.e))
        # self.paint.end()

app = QApplication(sys.argv)
ui = MainWindow()
ui.show()
sys.exit(app.exec_())
