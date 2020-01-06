from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(326, 317)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Number_min = QtWidgets.QLCDNumber(self.centralwidget)
        self.Number_min.setGeometry(QtCore.QRect(210, 40, 90, 40))
        self.Number_min.setObjectName("Number_min")
        self.Number_max = QtWidgets.QLCDNumber(self.centralwidget)
        self.Number_max.setGeometry(QtCore.QRect(210, 110, 90, 40))
        self.Number_max.setObjectName("Number_max")
        self.Number_sred = QtWidgets.QLCDNumber(self.centralwidget)
        self.Number_sred.setGeometry(QtCore.QRect(210, 180, 90, 40))
        self.Number_sred.setObjectName("Number_sred")
        self.min = QtWidgets.QLabel(self.centralwidget)
        self.min.setGeometry(QtCore.QRect(20, 40, 185, 40))
        self.min.setObjectName("min")
        self.max = QtWidgets.QLabel(self.centralwidget)
        self.max.setGeometry(QtCore.QRect(20, 110, 185, 40))
        self.max.setObjectName("max")
        self.sred = QtWidgets.QLabel(self.centralwidget)
        self.sred.setGeometry(QtCore.QRect(20, 180, 185, 40))
        self.sred.setObjectName("sred")
        MainWindow.setCentralWidget(self.centralwidget)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 250, 170, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.znach)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 325, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Файловая статистика"))
        self.min.setText(_translate("MainWindow", "Минимальное значение"))
        self.max.setText(_translate("MainWindow", "Максимальное значение"))
        self.sred.setText(_translate("MainWindow", "Среднее значение"))
        self.pushButton.setText(_translate("MainWindow", "Показать"))

    def znach(self):
        g = list(open("input.txt"))
        g_c = []
        for i in g:
            g_c.append(i.split())
        g.clear()
        for h in g_c:
            for j in h:
                g.append(int(j))
        mi = min(g)
        ma = max(g)
        sr = int(sum(g) / len(g))
        self.Number_min.display(mi)
        self.Number_max.display(ma)
        self.Number_sred.display(sr)
        u = open('output.txt', "w")
        u.write(f'{mi} {ma} {sr}')
        u.close()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
