try:
    from PyQt5.QtWidgets import *
    from PyQt5.QtGui import *
    from PyQt5.QtCore import *

except:
    from PyQt4.QtGui import *
    from PyQt4.QtCore import *

import sqlite3


class Widget(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Table')

        self.table_widget = QTableWidget()
        self.setCentralWidget(self.table_widget)

    def fill(self):
        self.table_widget.clear()

        labels = ['ID', 'NAME', 'PRICE', 'PRICE1']

        self.table_widget.setColumnCount(len(labels))
        self.table_widget.setHorizontalHeaderLabels(labels)
        # con = sqlite3.connect("baza.db")
        #
        # # Создание курсора
        # cur = con.cursor()
        #
        # # Выполнение запроса и получение всех результатов
        # #result = cur.execute("""SELECT * FROM Dohodi""").fetchall()
        # result = cur.execute("""SELECT summa, whre, data, year FROM Dohodi""").fetchall()
        # # Вывод результатов на экран
        # for elem in result:
        #     print(elem)

        # for tup in data:
        #     col = 0
        #
        #     for item in tup:
        #         cellinfo = QTableWidgetItem(item)
        #
        #         # Только для чтения
        #         cellinfo.setFlags(
        #             QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
        #         )
        #
        #         self.ui.tableWidget.setItem(row, col, cellinfo)
        #         col += 1
        #
        #     row += 1

        with sqlite3.connect("baza.db") as connect:
            for summa, whre, data, year in connect.execute("""SELECT * FROM Dohodi"""):
                row = self.table_widget.rowCount()
                self.table_widget.setRowCount(row + 1)
                self.table_widget.setItem(row, 0, QTableWidgetItem(str(summa)))
                self.table_widget.setItem(row, 1, QTableWidgetItem(whre))
                self.table_widget.setItem(row, 2, QTableWidgetItem(str(data)))
                self.table_widget.setItem(row, 3, QTableWidgetItem(str(year)))
                print(summa)
if __name__ == '__main__':
    app = QApplication([])

    w = Widget()
    w.show()
    w.fill()

    app.exec()