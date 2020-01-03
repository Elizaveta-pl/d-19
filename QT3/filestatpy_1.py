# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QT3/fileststui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(326, 317)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Number_min = QtWidgets.QLCDNumber(self.centralwidget)
        self.Number_min.setGeometry(QtCore.QRect(190, 40, 121, 41))
        self.Number_min.setObjectName("Number_min")
        self.Number_max = QtWidgets.QLCDNumber(self.centralwidget)
        self.Number_max.setGeometry(QtCore.QRect(190, 110, 121, 41))
        self.Number_max.setObjectName("Number_max")
        self.Number_sred = QtWidgets.QLCDNumber(self.centralwidget)
        self.Number_sred.setGeometry(QtCore.QRect(190, 180, 121, 41))
        self.Number_sred.setObjectName("Number_sred")
        self.min = QtWidgets.QLabel(self.centralwidget)
        self.min.setGeometry(QtCore.QRect(20, 40, 121, 41))
        self.min.setObjectName("min")
        self.max = QtWidgets.QLabel(self.centralwidget)
        self.max.setGeometry(QtCore.QRect(20, 110, 131, 41))
        self.max.setObjectName("max")
        self.sred = QtWidgets.QLabel(self.centralwidget)
        self.sred.setGeometry(QtCore.QRect(20, 180, 131, 41))
        self.sred.setObjectName("sred")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 230, 171, 31))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 326, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Файловая статистика"))
        self.min.setText(_translate("MainWindow", "Минимальное значение"))
        self.max.setText(_translate("MainWindow", "Максимальное значение"))
        self.sred.setText(_translate("MainWindow", "Среднее значение"))
        self.pushButton.setText(_translate("MainWindow", "Показать"))
