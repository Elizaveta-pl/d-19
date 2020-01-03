# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3, random


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        self.where_sql = 'title'
        self.where_sql_text = ''

        self.find_setting = {'title': '0', 'year': '1', 'duration': '2'}
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
        self.search()
        Dialog.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Dialog)
        self.statusbar.setObjectName("statusbar")
        Dialog.setStatusBar(self.statusbar)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def add_combo_box(self):
        for n in self.find_setting.keys():
            self.comboBox.addItem(n)

    def search(self):
        self.del_row()
        z = ['<', '>', '=']
        con = sqlite3.connect("films.db")
        cur = con.cursor()
        self.where_sql_text = f'"{self.textEdit.toPlainText()}"'
        if self.textEdit.toPlainText().strip() == "":
            text_sql = f'SELECT * FROM Films'
        elif (self.textEdit.toPlainText().strip().upper().startswith('LIKE')) \
                or (self.textEdit.toPlainText().strip()[0] in z):
            self.where_sql_text = self.textEdit.toPlainText().replace("'", '"')
            text_sql = f'SELECT * FROM Films  WHERE {self.where_sql} ' \
                       f'{self.where_sql_text} LIMIT 1'
        else:
            text_sql = f'SELECT * FROM Films  WHERE {self.where_sql} ' \
                       f'= {self.where_sql_text} LIMIT 1'
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

        self.where_sql = list(self.find_setting.keys())[
            self.comboBox.currentIndex()]

    def addrow(self, result):
        for i, row in enumerate(result):
            self.checkWidget.setRowCount(self.checkWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.checkWidget.setItem(i, j,
                                         QtWidgets.QTableWidgetItem(str(elem)))

        self.checkWidget.resizeColumnsToContents()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Поиск фильмов"))
        self.pushButton.setText(_translate("Dialog", "Найти"))
        self.comboBox.setItemText(0, _translate("Dialog", "Название"))
        self.comboBox.setItemText(1, _translate("Dialog", "Год выпуска"))
        self.comboBox.setItemText(2, _translate("Dialog", "Продолжительность"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QMainWindow()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
