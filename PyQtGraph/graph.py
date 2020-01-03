from PyQt5 import QtCore, QtGui, uic
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QListView, \
    QListWidget, QGridLayout, QPushButton, QLineEdit, QLabel
# from ui import Ui_Dialog
import sys  # We need sys so that we can pass argv to QApplication
import os

OPERATORS = {'+': (1, lambda x, y: x + y), '-': (1, lambda x, y: x - y),
             '*': (2, lambda x, y: x * y), '/': (2, lambda x, y: x / y),
             '$': (2, lambda x, y: (x ** (1 / y))), '^': (2, lambda x, y: x ** y)}


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.WindowModal)
        Dialog.resize(800, 600)

        self.gridLayoutWidget = QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(90, 20, 130, 80))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.lineGrapth = QLineEdit(Dialog)
        self.lineGrapth.setGeometry(QtCore.QRect(670, 30, 100, 25))
        self.lineGrapth.setObjectName("lineGrapth")
        self.label = QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(510, 30, 200, 25))
        self.label.setObjectName("label")

        self.label_r = QLabel(Dialog)
        self.label_r.setGeometry(QtCore.QRect(10, 30, 300, 25))
        self.label_r.setObjectName("label")

        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.graphicsView = PlotWidget(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(30, 80, 740, 440))
        self.graphicsView.setObjectName("graphicsView")

        self.pushBuild = QPushButton(Dialog)
        self.pushBuild.setGeometry(QtCore.QRect(680, 540, 90, 25))
        self.pushBuild.setObjectName("pushBuild")
        self.pushBuild.clicked.connect(self.parsing)

        # self.listViewGrapth.raise_()
        # self.listWidgetGrapth.raise_()
        self.gridLayoutWidget.raise_()
        self.graphicsView.raise_()
        self.pushBuild.raise_()
        self.lineGrapth.raise_()
        self.label.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def parsing(self):

        self.x = [i for i in range(1, 20)]
        self.y =[]
        # self.y = [2 / i for i in self.calc(self.sort(self.parse(self.lineGrapth.text().replace('x', self.x))))]
        for i in range(1, 20):
            formula = self.lineGrapth.text().replace('x', str(i))
            print(f'self.parse(formula = {list(self.parse(formula))}')
            pr = self.calc(self.sort(self.parse(self.lineGrapth.text().replace('x', str(i)))))
            self.y.append(pr)
        print(f' self.x = {self.x}')
        print(f' self.y = {self.y}')
        self.grapth()

    def grapth(self):
        self.graphicsView.clear()
        self.graphWidget = pg.PlotWidget()

        # self.x = [i for i in range(1, 20)]
        # self.y = [2 / i for i in self.x]
        # print(self.x)
        # print(self.y)
        # self.graphicsView(self.graphWidget)
        # self.setCentralWidget(self.graphWidget)

        hour = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        temperature = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]

        # plot data: x, y values
        self.graphicsView.plot(self.x, self.y, pen='g')

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Графики"))
        self.pushBuild.setText(_translate("Dialog", "Построить"))
        self.label.setText(_translate("Dialog", "Добавить формулу y ="))
        self.label_r.setText(
            _translate("Dialog", "Формула записывается через пробел"))

    def parse(self, line):
        print(f'line = {line}')
        num = ''
        for i in line:
            if i in '1234567890.':
                num += i
            elif num:
                yield float(num)
                num = ''
            if i in OPERATORS or i in '()':
                yield i
        if num:
            yield float(num)

    def sort(self, parsed):
        tmp = []
        for i in parsed:
            if i in OPERATORS:
                while tmp and tmp[-1] != '(' and OPERATORS[i][0] <= \
                        OPERATORS[tmp[-1]][0]:
                    yield tmp.pop()
                tmp.append(i)
            elif i == ')':
                while tmp:
                    x = tmp.pop()
                    if x == '(':
                        break
                    yield x
            elif i == '(':
                tmp.append(i)
            else:
                yield i
        while tmp:
            yield tmp.pop()

    def calc(self, sort):
        print(f'sort = {sort}')
        tmp = []
        for i in sort:
            print(f'i = {i}')
            if i in OPERATORS:
                y = tmp.pop()
                x = tmp.pop()
                print(f' x = {x}, y = {y}')
                tmp.append(OPERATORS[i][1](x, y))
            else:
                tmp.append(i)
        return tmp[0]


# class MainWindow(QMainWindow, Ui_Dialog):
#     def __init__(self, parent=None, *args, **kwargs):
#         QMainWindow.__init__(self)
#         self.setupUi(self)

class MainWindow(QMainWindow, Ui_Dialog):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
