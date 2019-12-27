import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget, \
    QTableWidgetItem, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QColor
import csv, random


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 table - pythonspot.com'
        self.left = 0
        self.top = 0
        self.width = 500
        self.height = 500
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createTable()

        # Add box layout, add table to box layout and add box layout to widget
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)

        # Show widget
        self.show()
        self.loadTable()

    def createTable(self):
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.move(0, 0)

    def loadTable(self):
        h = 0
        with open('wares.csv', encoding="utf8") as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            # title1 = next(reader)
            # print(type(title1))
            title1 = sorted(list(reader), key=lambda item: item[1], reverse=True)
            print(type(title1))
            self.tableWidget.setColumnCount(len(title1))
            self.tableWidget.setHorizontalHeaderLabels(title1)
            self.tableWidget.setRowCount(0)
            for i, row in enumerate(reader):
                h += 1
                self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
                for j, elem in enumerate(row):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(elem))
                    if h <= 5:
                        self.colorRow(i, QColor(random.randint(0, 255), random.randint(0, 255),
                                                random.randint(0, 255)))
        self.tableWidget.resizeColumnsToContents()

    def colorRow(self, row, color):
        # for i in range(self.tableWidget.columnCount()):
        #     self.tableWidget.item(row, i).setBackground(color)
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
