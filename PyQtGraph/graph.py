from PyQt5 import QtCore, QtGui, uic
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QListView,\
    QListWidget, QGridLayout, QPushButton, QLineEdit, QLabel
# from ui import Ui_Dialog
import sys  # We need sys so that we can pass argv to QApplication
import os


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

        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.graphicsView = PlotWidget(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(30, 80, 740, 440))
        self.graphicsView.setObjectName("graphicsView")

        self.pushBuild = QPushButton(Dialog)
        self.pushBuild.setGeometry(QtCore.QRect(680, 540, 90, 25))
        self.pushBuild.setObjectName("pushBuild")
        self.pushBuild.clicked.connect(self.grapth)

        # self.listViewGrapth.raise_()
        # self.listWidgetGrapth.raise_()
        self.gridLayoutWidget.raise_()
        self.graphicsView.raise_()
        self.pushBuild.raise_()
        self.lineGrapth.raise_()
        self.label.raise_()


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def grapth(self):
        self.graphicsView.clear()
        self.graphWidget = pg.PlotWidget()

        self.x = [i for i in range(1, 20)]
        self.y = [2 / i for i in self.x]
        print(self.x)
        print(self.y)
        # self.graphicsView(self.graphWidget)
        # self.setCentralWidget(self.graphWidget)

        hour = [1,2,3,4,5,6,7,8,9,10]
        temperature = [30,32,34,32,33,31,29,32,35,45]

        # plot data: x, y values
        self.graphicsView.plot(self.x, self.y, pen='g')

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Графики"))
        self.pushBuild.setText(_translate("Dialog", "Построить"))
        self.label.setText(_translate("Dialog", "Добавить формулу y ="))


# class MainWindow(QMainWindow, Ui_Dialog):
#     def __init__(self, parent=None, *args, **kwargs):
#         QMainWindow.__init__(self)
#         self.setupUi(self)

class MainWindow(QMainWindow, Ui_Dialog):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)



def main():
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()