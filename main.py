from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sqlite3
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        self.pushButton.clicked.connect(self.fill)

    def fill(self):
        print1


app = QApplication(sys.argv)
ui = MainWindow()
ui.show()
sys.exit(app.exec_())
