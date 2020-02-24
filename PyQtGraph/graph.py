from PyQt5 import QtCore
from pyqtgraph import PlotWidget
import pyqtgraph as pg

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QGridLayout, \
    QPushButton, QLineEdit, QLabel
import sys

operators = {'+': (1, lambda x, y: x + y), '-': (1, lambda x, y: x - y),
             '*': (2, lambda x, y: x * y), '/': (2, lambda x, y: x / y),
             'v': (2, lambda x, y: (x ** (1 / y))), '^': (2, lambda x, y: x ** y)}


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
        self.label_r.setGeometry(QtCore.QRect(10, 30, 400, 25))
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

        self.label_2 = QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 111, 21))
        self.label_2.setObjectName("label_2")

        self.lineEdit_xk = QLineEdit(Dialog)
        self.lineEdit_xk.setGeometry(QtCore.QRect(150, 10, 21, 20))
        self.lineEdit_xk.setObjectName("lineEdit_xk")

        self.lineEdit_xn = QLineEdit(Dialog)
        self.lineEdit_xn.setGeometry(QtCore.QRect(120, 10, 21, 20))
        self.lineEdit_xn.setObjectName("lineEdit_xn")

        self.gridLayoutWidget.raise_()
        self.graphicsView.raise_()
        self.pushBuild.raise_()
        self.lineGrapth.raise_()
        self.label.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def parsing(self):

        self.x = [i for i in range(int(self.lineEdit_xn.text()), int(self.lineEdit_xk.text()))]
        self.y = []
        for i in range(int(self.lineEdit_xn.text()), int(self.lineEdit_xk.text())):
            pr = self.calc(self.sort(self.parse(self.lineGrapth.text().replace('x', str(i)))))
            self.y.append(pr)
        self.grapth()

    def grapth(self):
        self.graphicsView.clear()
        self.graphWidget = pg.PlotWidget()
        self.graphicsView.plot(self.x, self.y, pen='g')

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Графики"))
        self.pushBuild.setText(_translate("Dialog", "Построить"))
        self.label.setText(_translate("Dialog", "Добавить формулу y ="))
        self.label_r.setText(
            _translate("Dialog", "В написании формулы для возведения в степень используйте '^', \n"
                                 "а для нахождения корня 'v'"))
        self.label_2.setText(_translate("Dialog", "Введите диапозон х"))

    def parse(self, line):
        num = ''
        for i in line:
            if i in '1234567890.':
                num += i
            elif num:
                yield float(num)
                num = ''
            if i in operators or i in '()':
                yield i
        if num:
            yield float(num)

    def sort(self, parsed):
        cal = []
        for i in parsed:
            if i in operators:
                while cal and cal[-1] != '(' and operators[i][0] <= operators[cal[-1]][0]:
                    yield cal.pop()
                cal.append(i)
            elif i == ')':
                while cal:
                    x = cal.pop()
                    if x == '(':
                        break
                    yield x
            elif i == '(':
                cal.append(i)
            else:
                yield i
        while cal:
            yield cal.pop()

    def calc(self, sort):
        cal = []
        for i in sort:
            if i in operators:
                y = cal.pop()
                x = cal.pop()
                cal.append(operators[i][1](x, y))
            else:
                cal.append(i)
        return cal[0]


class MainWindow(QMainWindow, Ui_Dialog):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
