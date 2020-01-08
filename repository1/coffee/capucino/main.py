from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import sys



class ClssDialog(QDialog):
    def __init__(self, parent=None):
        super(ClssDialog, self).__init__(parent)
        uic.loadUi('addEditCoffeeForm_v1.ui', self)
        self.pushButton_save.clicked.connect(
            self.save)  # Сохранить данные

    def save(self):
        print(3)
    # def btnClosed(self):
    #     self.close()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.pushButton.clicked.connect(self.fill)
        self.pushButton_add.clicked.connect(
            self.open_dialog)  # Открыть новую форму для добавления
        self.pushButton_edit.clicked.connect(
            self.open_dialog)  # Открыть новую форму для редактирования


    def fill(self):
        self.tableWidget.clear()
        self.del_row()

        labels = ['ID', 'Название сорта', 'Степень обжарки', 'Молотый/в зернах',
                  'Описание вкуса', 'Цена', 'Объем упаковки']

        self.tableWidget.setColumnCount(len(labels))
        self.tableWidget.setHorizontalHeaderLabels(labels)
        with sqlite3.connect("coffee.db") as connect:
            for ID, Name, Stepen, Tip, Opisanie, Cena, Obem in connect.execute(
                    """SELECT * FROM price where ID > 0"""):
                row = self.tableWidget.rowCount()
                self.tableWidget.setRowCount(row + 1)
                self.tableWidget.setItem(row, 0, QTableWidgetItem(str(ID)))
                self.tableWidget.setItem(row, 1, QTableWidgetItem(Name))
                self.tableWidget.setItem(row, 2, QTableWidgetItem(Stepen))
                self.tableWidget.setItem(row, 3, QTableWidgetItem(Tip))
                self.tableWidget.setItem(row, 4, QTableWidgetItem(Opisanie))
                self.tableWidget.setItem(row, 5, QTableWidgetItem(str(Cena)))
                self.tableWidget.setItem(row, 6, QTableWidgetItem(str(Obem)))

        self.tableWidget.resizeColumnsToContents()

    def del_row(self):
        for d in range(self.tableWidget.rowCount()):
            self.tableWidget.removeRow(0)


    def open_dialog(self):
        dialog = ClssDialog(self)
        dialog.exec_()


app = QApplication(sys.argv)
ui = MainWindow()
ui.show()
sys.exit(app.exec_())
