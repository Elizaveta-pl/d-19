# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import csv


class Ui_Dialog(object):

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Dialog)
        self.centralwidget.setObjectName("centralwidget")
        self.checkWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.checkWidget.setGeometry(QtCore.QRect(20, 50, 750, 480))
        self.checkWidget.setObjectName("checkWidget")
        self.checkWidget.setColumnCount(0)
        self.checkWidget.setRowCount(0)
        self.checkWidget.setMouseTracking(True)
        self.checkWidget.setTabKeyNavigation(True)

        self.comboBoxShool = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxShool.setGeometry(QtCore.QRect(90, 10, 80, 25))
        self.comboBoxShool.setObjectName("comboBox")
        self.comboBoxShool.currentIndexChanged.connect(
            self.selectionchange)
        self.comboBoxKlass = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxKlass.setGeometry(QtCore.QRect(260, 10, 80, 25))
        self.comboBoxKlass.setObjectName("comboBox")
        self.comboBoxKlass.currentIndexChanged.connect(
            self.selectionchange)

        self.read_csv()
        self.add_combo_box()
        self.search()

        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(30, 10, 80, 25))
        self.label_1.setObjectName("label_1")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(210, 10, 80, 25))
        self.label_2.setObjectName("label_2")

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
        Dialog.setWindowTitle(_translate("Dialog", "Олимпиада"))
        self.label_1.setText(_translate("Dialog", "Школа"))
        self.label_2.setText(_translate("Dialog", "Класс"))

    def read_csv(self):
        with open('rez.csv', encoding="utf8") as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            self.result = []
            result_new = []
            for row in list(reader)[1:]:
                row_new = []
                row_new.append(row[0])
                row_new.append(f'{row[1].split()[3]} {row[1].split()[4]}')
                row_new.append(row[2])
                row_new.append(row[7])

                row_new.append(row[2].split('-')[2])
                row_new.append(row[2].split('-')[3])
                result_new.append(row_new)
                self.result.append(row)

            self.login = [row[2].split('-') for row in self.result]
            self.shool = [i[2] for i in self.login]
            self.klass = [i[3] for i in self.login]
            self.klass.append('')
            self.shool.append('')
            self.shool = list(set(self.shool))
            self.klass = list(set(self.klass))

            self.result = result_new

    def activatedRowColumn(self, r, c):
        pass

    def changedRowColumn(self, r, c):
        pass

    def clickedRowColumn(self, r, c):
        pass

    def enteredRowColumn(self, r, c):
        pass

    def add_combo_box(self):
        for n in self.shool:
            self.comboBoxShool.addItem(n)
        for n in self.klass:
            self.comboBoxKlass.addItem(n)

    def selectionchange(self, i):
        klass = self.comboBoxKlass.currentText()
        shool = self.comboBoxShool.currentText()
        if klass == '' and shool == '':
            result = [row for row in self.result]
        elif klass == '':
            result = [row for row in self.result if row[4] == shool]
        elif shool == '':
            result = [row for row in self.result if row[5] == klass]
        else:
            result = [row for row in self.result if
                      (row[4] == shool or row[5] == klass)]
        self.addrow(result)

    def del_row(self):
        for d in range(self.checkWidget.rowCount()):
            self.checkWidget.removeRow(0)

    def search(self):
        # names_title = ['Место', 'Имя участника', 'Логин', 'Задача1',
        #                'Задача2', 'Задача3', 'Задача4', 'Сумма баллов']
        names_title = ['Место', 'Имя участника', 'Логин', 'Сумма баллов']
        self.checkWidget.setColumnCount(len(names_title))
        self.checkWidget.setHorizontalHeaderLabels(names_title)

        self.addrow(self.result)

    def addrow(self, result):
        self.del_row()
        for i, row in enumerate(result):
            self.checkWidget.setRowCount(self.checkWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                item = QtWidgets.QTableWidgetItem(str(elem))
                self.checkWidget.setItem(i, j, item)

        self.checkWidget.resizeColumnsToContents()
        self.checkWidget.sortItems(0, QtCore.Qt.AscendingOrder)
        self.checkWidget.colorCount()

        item1 = self.checkWidget.item(0, 0)
        if item1 != None:
            if self.checkWidget.rowCount() >= 3:
                row_color = 3
            else:
                row_color = self.checkWidget.rowCount()

            for i in range(row_color):
                for j in range(self.checkWidget.columnCount()):
                    self.checkWidget.item(i, j).setBackground(
                        QtGui.QColor(100, 100, 150))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QMainWindow()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
