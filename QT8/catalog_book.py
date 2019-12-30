# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3, random

class Ui_Dialog(object):
    def setupUi(self, Dialog):

        self.where_sql = 'title'
        self.where_sql_text = ''

        self.find_setting = {'title': '0', 'year': '1', 'duration': '2'}

        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(Dialog)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 390, 101, 30))
        self.pushButton.setObjectName("pushButton")
        self.checkWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.checkWidget.setGeometry(QtCore.QRect(20, 50, 600, 330))
        self.checkWidget.setObjectName("checkWidget")
        self.checkWidget.setColumnCount(0)
        self.checkWidget.setRowCount(0)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(20, 10, 180, 30))
        self.comboBox.setObjectName("comboBox")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(210, 10, 250, 30))
        self.textEdit.setObjectName("textEdit")
        Dialog.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Dialog)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 22))
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
        self.comboBox.setItemText(0, _translate("Dialog", "Название"))
        self.comboBox.setItemText(1, _translate("Dialog", "Автор"))

    def add_combo_box(self):
        for n in self.find_setting.keys():
            self.comboBox.addItem(n)

    def selectionchange(self, i):
        self.where_sql = list(self.find_setting.keys())[
            self.comboBox.currentIndex()]

    def del_row(self):
        for d in range(self.checkWidget.rowCount()):
            self.checkWidget.removeRow(0)

    def search(self):
        self.del_row()
        z = ['<', '>', '=']
        con = sqlite3.connect("films.db")
        cur = con.cursor()

        self.where_sql_text = f'"{self.textEdit.toPlainText()}"'
        text_sql = f'SELECT * FROM Films  WHERE {self.where_sql} ' \
                   f'= {self.where_sql_text} LIMIT 1'

        if self.textEdit.toPlainText().strip().upper().startswith('LIKE'):
            pass
        elif self.textEdit.toPlainText().strip()[0] in z:
            pass
        else:
            self.textEdit.setPlainText('= ' + self.textEdit.toPlainText())

        self.textEdit.setPlainText(
            self.textEdit.toPlainText().replace("'", '"'))

        text_sql = f'SELECT * FROM Films  WHERE  {self.where_sql}' \
                   f' {self.textEdit.toPlainText()} LIMIT 1'
        result = cur.execute(text_sql)
        names_title = [description[0] for description in result.description]
        self.checkWidget.setColumnCount(len(names_title))
        self.checkWidget.setHorizontalHeaderLabels(names_title)

        self.addrow(result)
        con.close()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QMainWindow()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
