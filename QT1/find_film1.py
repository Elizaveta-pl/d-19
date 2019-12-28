# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QT1/ui/find.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3, random


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
        self.pushButton.clicked.connect(self.search)
        self.checkWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.checkWidget.setGeometry(QtCore.QRect(20, 50, 450, 250))
        self.checkWidget.setObjectName("checkWidget")
        self.checkWidget.setColumnCount(0)
        self.checkWidget.setRowCount(0)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 10, 131, 25))
        self.comboBox.setObjectName("comboBox")
        self.add_combo_box()

        self.comboBox.activated[str].connect(self.onActivated)
        self.comboBox.currentIndexChanged.connect(self.selectionchange)

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

        self.toolbutton = QtWidgets.QToolButton(self.centralwidget)
        self.toolbutton.setGeometry(QtCore.QRect(120, 300, 89, 25))
        self.toolbutton.setText('Select Categories ')
        self.toolmenu = QtWidgets.QMenu()
        for i in range(3):
            action = self.toolmenu.addAction("Category " + str(i))
            action.setCheckable(True)
        self.toolbutton.setMenu(self.toolmenu)
        self.toolbutton.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.toolbutton.setFixedSize(16, 16)

        # self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        #
        # self.pushButton.setObjectName("pushButton")
        # Dialog.addWidget(self.toolbutton)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def add_combo_box(self):
        for n in self.find_setting:
            self.comboBox.addItem(n)

    def search(self):
        # con = sqlite3.connect(input())
        con = sqlite3.connect("films.db")

        cur = con.cursor()

        # result = cur.execute("""SELECT title FROM Films
        #                         WHERE duration >= 60 and genre=(SELECT id FROM genres'
        #                      ' WHERE  title = "комедия") """).fetchall()
        result = cur.execute("""SELECT * FROM Films
                                        WHERE duration >= 1680 """)
        # names = result.keys()
        names_title = [description[0] for description in result.description]
        self.checkWidget.setColumnCount(len(names_title))
        self.checkWidget.setHorizontalHeaderLabels(names_title)

        self.addrow(result)
        con.close()

    def onActivated(self, i):

        if str == "Название":
            print(i)

    def selectionchange(self, i):

        for count in range(self.comboBox.count()):
            print(self.comboBox.itemText(count))
        print("Current index", i, "selection changed ",
              self.comboBox.currentText())
    def addrow(self, result):
        for i, row in enumerate(result):
            # print(row)
            self.checkWidget.setRowCount(self.checkWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                print(f'elem = {elem}, i = {i}, j = {j}')
                self.checkWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(elem)))
                # if h <= 5:
                #     self.colorRow(i, QtWidgets.QColor(random.randint(0, 255),
                #                             random.randint(0, 255),
                #                             random.randint(0, 255)))
        # делаем ресайз колонок по содержимому
        self.checkWidget.resizeColumnsToContents()


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Поиск фильмов"))
        self.pushButton.setText(_translate("Dialog", "Найти"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QMainWindow()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
