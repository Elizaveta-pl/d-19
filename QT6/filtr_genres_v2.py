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
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(Dialog)
        self.centralwidget.setObjectName("centralwidget")

        self.checkWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.checkWidget.setGeometry(QtCore.QRect(20, 50, 600, 370))
        self.checkWidget.setObjectName("checkWidget")
        self.checkWidget.setColumnCount(0)
        self.checkWidget.setRowCount(0)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(380, 10, 235, 25))
        self.comboBox.setObjectName("comboBox")
        self.add_combo_box()
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 10, 135, 20))
        self.label.setObjectName("label")

        self.comboBox.activated[str].connect(self.onActivated)
        self.comboBox.currentIndexChanged.connect(self.selectionchange)

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
        con = sqlite3.connect("films.db")
        cur = con.cursor()
        result = cur.execute("SELECT * FROM genres")
        for n in result:
            self.comboBox.addItem(n[1], n[0])

    def search(self):

        self.del_row()
        con = sqlite3.connect("films.db")
        cur = con.cursor()
        text_sql = f'SELECT * FROM Films  WHERE  genre = {self.comboBox.currentData()} '
        result = cur.execute(text_sql)
        names_title = [description[0] for description in result.description]
        self.checkWidget.setColumnCount(len(names_title))
        self.checkWidget.setHorizontalHeaderLabels(names_title)

        self.addrow(result)
        con.close()

    def del_row(self):
        for d in range(self.checkWidget.rowCount()):
            self.checkWidget.removeRow(0)

    def onActivated(self, i):
        pass

    def selectionchange(self, i):
        for count in range(self.comboBox.count()):
            print(self.comboBox.itemText(count))
        self.search()

    def addrow(self, result):
        con = sqlite3.connect("films.db")
        cur = con.cursor()

        for i, row in enumerate(result):
            self.checkWidget.setRowCount(self.checkWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.checkWidget.setItem(i, j,
                                         QtWidgets.QTableWidgetItem(str(elem)))
        self.checkWidget.resizeColumnsToContents()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Отбор фильмов по жанрам"))
        self.label.setText(_translate("Dialog", "Отфильтровать по:"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QMainWindow()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
