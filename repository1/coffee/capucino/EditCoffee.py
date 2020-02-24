from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import *
import sqlite3
import sys


class EditCoffeeForm(object):
    def setupUi(self, Form):
    # def __init__(self):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)

        Form.setObjectName("Внесите данные")
        Form.resize(395, 294)

        self.pushButton.clicked.connect(self.fill)

        self.retranslateUi(Form)

        QtCore.QMetaObject.connectSlotsByName(Form)

# app = QApplication(sys.argv)
# ui = MainWindow()
# ui.show()
# sys.exit(app.exec_())
