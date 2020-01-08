# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QT8/ui/book.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Dialog)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(330, 510, 101, 31))
        self.pushButton.setObjectName("pushButton")
        self.checkWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.checkWidget.setGeometry(QtCore.QRect(20, 50, 501, 451))
        self.checkWidget.setObjectName("checkWidget")
        self.checkWidget.setColumnCount(0)
        self.checkWidget.setRowCount(0)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(20, 10, 180, 30))
        self.comboBox.setObjectName("comboBox")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(270, 10, 250, 30))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(600, 10, 131, 181))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(530, 210, 251, 31))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(530, 240, 261, 31))
        self.label_title.setText("")
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.label_autor = QtWidgets.QLabel(self.centralwidget)
        self.label_autor.setGeometry(QtCore.QRect(530, 300, 261, 31))
        self.label_autor.setText("")
        self.label_autor.setAlignment(QtCore.Qt.AlignCenter)
        self.label_autor.setObjectName("label_autor")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(530, 270, 251, 31))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_year = QtWidgets.QLabel(self.centralwidget)
        self.label_year.setGeometry(QtCore.QRect(530, 360, 261, 31))
        self.label_year.setText("")
        self.label_year.setAlignment(QtCore.Qt.AlignCenter)
        self.label_year.setObjectName("label_year")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(530, 330, 261, 31))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(530, 390, 261, 31))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_genre = QtWidgets.QLabel(self.centralwidget)
        self.label_genre.setGeometry(QtCore.QRect(530, 420, 261, 31))
        self.label_genre.setText("")
        self.label_genre.setAlignment(QtCore.Qt.AlignCenter)
        self.label_genre.setObjectName("label_genre")
        Dialog.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Dialog)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        Dialog.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Dialog)
        self.statusbar.setObjectName("statusbar")
        Dialog.setStatusBar(self.statusbar)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Каталог библиотеки"))
        self.pushButton.setText(_translate("Dialog", "Найти"))
        self.label.setText(_translate("Dialog", "TextLabel"))
        self.label_2.setText(_translate("Dialog", "Наименование"))
        self.label_3.setText(_translate("Dialog", "Автор"))
        self.label_4.setText(_translate("Dialog", "Год выпуска"))
        self.label_5.setText(_translate("Dialog", "Жанр"))
