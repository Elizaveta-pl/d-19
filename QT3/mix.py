# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QT3/mix.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(946, 602)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn = QtWidgets.QPushButton(self.centralwidget)
        self.btn.setGeometry(QtCore.QRect(320, 450, 291, 71))
        self.btn.setObjectName("btn")
        self.ListWidget_c = QtWidgets.QListView(self.centralwidget)
        self.ListWidget_c.setGeometry(QtCore.QRect(10, 20, 451, 391))
        self.ListWidget_c.setObjectName("ListWidget_c")
        self.ListWidget_nc = QtWidgets.QListWidget(self.centralwidget)
        self.ListWidget_nc.setGeometry(QtCore.QRect(470, 20, 461, 391))
        self.ListWidget_nc.setObjectName("ListWidget_nc")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 946, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Mix"))
        self.btn.setText(_translate("MainWindow", "Вывести"))
