# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QT1/ui/find.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        self.find_setting = ['Название', 'Год выпуска', 'Продолжительность']
        Dialog.setObjectName("Dialog")
        Dialog.resize(565, 438)
        self.centralwidget = QtWidgets.QWidget(Dialog)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 350, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.checkWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.checkWidget.setGeometry(QtCore.QRect(270, 110, 256, 161))
        self.checkWidget.setObjectName("checkWidget")
        self.checkWidget.setColumnCount(0)
        self.checkWidget.setRowCount(0)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 10, 131, 25))
        self.comboBox.setObjectName("comboBox")
        for n in self.find_setting:
            self.comboBox.addItem(self, n)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(163, 10, 221, 31))
        self.textEdit.setObjectName("textEdit")
        Dialog.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Dialog)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 565, 22))
        self.menubar.setObjectName("menubar")
        Dialog.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Dialog)
        self.statusbar.setObjectName("statusbar")
        Dialog.setStatusBar(self.statusbar)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def add_combo_box(self):
        for n in self.find_setting:
            self.comboBox.addItem(self, n)
        pass

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Поиск фильмов"))
        self.pushButton.setText(_translate("Dialog", "Заказать"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QMainWindow()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
