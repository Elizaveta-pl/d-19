# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PyQtGraph/ui/grapth1.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.WindowModal)
        Dialog.resize(727, 504)
        self.listViewGrapth = QtWidgets.QListView(Dialog)
        self.listViewGrapth.setGeometry(QtCore.QRect(40, 110, 301, 261))
        self.listViewGrapth.setObjectName("listViewGrapth")
        self.listWidgetGrapth = QtWidgets.QListWidget(Dialog)
        self.listWidgetGrapth.setGeometry(QtCore.QRect(380, 110, 301, 261))
        self.listWidgetGrapth.setObjectName("listWidgetGrapth")
        self.pushBuild = QtWidgets.QPushButton(Dialog)
        self.pushBuild.setGeometry(QtCore.QRect(440, 440, 89, 25))
        self.pushBuild.setObjectName("pushBuild")
        self.lineGrapth = QtWidgets.QLineEdit(Dialog)
        self.lineGrapth.setGeometry(QtCore.QRect(490, 30, 171, 25))
        self.lineGrapth.setObjectName("lineGrapth")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(290, 30, 201, 20))
        self.label.setObjectName("label")
        self.check = QtWidgets.QPlainTextEdit(Dialog)
        self.check.setGeometry(QtCore.QRect(120, 400, 104, 70))
        self.check.setObjectName("check")
        self.Gamburger = QtWidgets.QCheckBox(Dialog)
        self.Gamburger.setGeometry(QtCore.QRect(90, 50, 92, 23))
        self.Gamburger.setChecked(False)
        self.Gamburger.setObjectName("Gamburger")
        self.listViewGrapth.raise_()
        self.pushBuild.raise_()
        self.lineGrapth.raise_()
        self.label.raise_()
        self.listWidgetGrapth.raise_()
        self.check.raise_()
        self.Gamburger.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Графики"))
        self.pushBuild.setText(_translate("Dialog", "Построить"))
        self.label.setText(_translate("Dialog", "Добавить формулу"))
        self.Gamburger.setText(_translate("Dialog", "Гамбургер"))
