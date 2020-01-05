# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3, random, sys
import sys

from PyQt5.QtWidgets import QWidget, QApplication


class Ui_Dialog(object):
    def setupUi(self, Dialog):

        self.where_sql = 'title'
        self.where_sql_text = ''
        self.find_setting = {'title': '0', 'autor': '1'}
        # self.p_text.keyPressEvent = self.keyPressEvent

        # self.keymap = {QtCore.Qt.Key_Left: _board.tryLeft,
        #                QtCore.Qt.Key_Right: _board.tryRight,
        #                QtCore.Qt.Key_Up: _board.tryRorateCCW,
        #                QtCore.Qt.Key_Down: _board.tryRorateCCW,
        #                QtCore.Qt.Key_Space: _board.dropDown,
        #                QtCore.Qt.Key_D: _board.tryLineDown}


        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Dialog)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 530, 100, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.keyPressEvent)

        # # Add paint widget and paint
        # self.m = PaintWidget(self)
        # self.m.move(0, 100)
        # self.m.resize(self.width, self.height)


        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 10, 130, 280))
        self.label.setObjectName("label")

        self.label_p = QtWidgets.QLabel(self.centralwidget)
        self.label_p.setGeometry(QtCore.QRect(280, 10, 130, 280))
        self.label_p.setObjectName("label")

        self.pixmap = QtGui.QPixmap('jpg/blezs.jpg').scaledToHeight(300)

        self.label.setPixmap(self.pixmap)
        self.label.resize(180, 300)

        # self.label_p.setPixmap(self.pixmap)
        # self.label_p.resize(180, 300)

        # Add paint widget and paint
        # self.m = PaintWidget(Dialog)
        # self.m.move(10, 400)
        # self.label.setPicture(self.m)
        # self.label.resize(120, 200)
        # self.label.move(200, 200)
        # self.resize(self.pixmap.width(), self.pixmap.height())

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
        Dialog.setWindowTitle(_translate("Dialog", "Рисование"))
        self.pushButton.setText(_translate("Dialog", "Нарисовать"))

# class PaintWidget(QWidget):
    # def paintEvent(self, event):
    #     qp = QPainter(self)
    #
    #     # qp.setPen(Qt.black)
    #     size = self.size()
    #
    #     for i in range(1024):
    #         x = random.randint(1, size.width()-1)
    #         y = random.randint(1, size.height()-1)
    #         qp.drawPoint(x, y)


    #
    def paintEvent(self, event):

        pixmap = QtGui.QPixmap(self.size())
        self.mPixmap = pixmap
        pixmap.fill(QtCore.Qt.white)
        painter = QtGui.QPainter(pixmap)
        painter.drawPixmap(0, 0, self.mPixmap)

        painter.begin(self)

        self.drawFlag(painter)

        painter.end()

        # self.drawBackground(painter)



        # print('123')
        # qp = QtGui.QPainter(self)
        # qp.begin(self)
        # qp.drawEllipse(QtCore.QPoint(100, 100), 60, 60)
        #
        # qp.drawEllipse(QtCore.QPoint(100, 100), 60, 60)
        # # set color for pen by property
        # qp.setPen(QtGui.QPen(QtCore.Qt.blue, 3, join=QtCore.Qt.MiterJoin))
        # # draw a rectangle
        # qp.drawRect(80, 160, 100, 100)
        # # set color for pen by Qt color
        # qp.setPen(QtGui.QPen(QtCore.Qt.red, 2))
        # # set brush
        # my_brush = QtGui.QBrush(QColor(33, 33, 100, 255), QtCore.Qt.DiagCrossPattern)
        # qp.setBrush(my_brush)
        # # draw a rectangle and fill with the brush
        # qp.drawRect(300, 300, 180, 180)
        # print('124')
        #
        # qp.end()

    # def draw(self):
    #     pass
    #



    def drawFlag(self, qp):
        print('147')
        qp.setBrush(QtGui.QColor(255, 0, 0))
        qp.drawRect(30, 30, 120, 30)
        qp.setBrush(QtGui.QColor(0, 255, 0))
        qp.drawRect(30, 60, 120, 30)
        qp.setBrush(QtGui.QColor(0, 0, 255))
        qp.drawRect(30, 90, 120, 30)


        self.update()

    def keyPressEvent(self, event):
        # gey = event.key()
        # self.func = (None, None)
        update()

        # brush = QtGui.QBrush(QtCore.Qt.SolidPattern)
        # qp.setBrush(brush)
        # qp.drawRect(10, 15, 120, 90)
        #
        # brush.setStyle(QtCore.Qt.VerPattern)
        # qp.setBrush(brush)
        # qp.drawRect(130, 195, 90, 60)

        # brush.setStyle(QtCore.Qt.BDiagPattern)
        # qp.setBrush(brush)
        # qp.drawRect(250, 195, 90, 60)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QMainWindow()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)

    # # Add paint widget and paint
    # m = PaintWidget(Dialog)
    # m.move(10, 400)
    # width = 20
    # height = 40
    # # m.resize(width, height)

    Dialog.show()
    sys.exit(app.exec_())