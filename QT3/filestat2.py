from PyQt5 import QtCore, QtGui, QtWidgets

stat = {'a': '', 'b': '', 'c': '', 'd': '', 'e': '', 'f': '',
        'g': '', 'h': '', 'i': '', 'j': '', 'k': '', 'l': '',
        'm': '', 'n': '', 'o': '', 'p': '', 'q': '', 'r': '',
        's': '', 't': '', 'u': '', 'v': '', 'w': '', 'x': '',
        'y': '', 'z': '', 'а': '', 'б': '', 'в': '', 'г': '', 'д': '', 'е': '',
        'ё': '', 'ж': '', 'з': '', 'и': '', 'й': '', 'к': '',
        'л': '', 'м': '', 'н': '', 'о': '', 'п': '', 'р': '',
        'с': '', 'т': '', 'у': '', 'ф': '', 'х': '', 'ц': '',
        'ч': '', 'ш': '', 'щ': '', 'ы': '', 'э': '', 'ю': '',
        'я': '', '1': '', '2': '', '3': '', '4': '',
        '5': '', '6': '', '7': '',
        '8': '', '9': '', '0': ''}


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(468, 309)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.max = QtWidgets.QLabel(self.centralwidget)
        self.max.setGeometry(QtCore.QRect(10, 50, 201, 31))
        self.max.setObjectName("max")
        self.min = QtWidgets.QLabel(self.centralwidget)
        self.min.setGeometry(QtCore.QRect(10, 130, 201, 41))
        self.min.setObjectName("min")
        self.lcdNumber_max = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_max.setGeometry(QtCore.QRect(330, 50, 91, 41))
        self.lcdNumber_max.setObjectName("lcdNumber_max")
        self.lcdNumber_min = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_min.setGeometry(QtCore.QRect(330, 130, 91, 41))
        self.lcdNumber_min.setObjectName("lcdNumber_min")
        self.textEdit_max = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_max.setGeometry(QtCore.QRect(220, 50, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit_max.setFont(font)
        self.textEdit_max.setObjectName("textEdit_max")
        self.textEdit_min = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_min.setGeometry(QtCore.QRect(220, 130, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit_min.setFont(font)
        self.textEdit_min.setObjectName("textEdit_min")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 210, 211, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.znach)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 468, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Файловая статистика 2"))
        self.max.setText(_translate("MainWindow", "Самый часто встречающийся символ"))
        self.min.setText(_translate("MainWindow", "Самый редко встречающийся символ"))
        self.pushButton.setText(_translate("MainWindow", "Показать"))

    def znach(self):
        g = list(open('input.txt'))
        print(g)
        g_c = []
        for i in g:
            print(i)
            g_c.append(i.split())
        g.clear()
        # for h in g_c:
        #     for j in h:
        #         g.append(int(j))
        # mi = min(g)
        # ma = max(g)
        # sr = int(sum(g) / len(g))
        # self.Number_min.display(mi)
        # self.Number_max.display(ma)
        # self.Number_sred.display(sr)
        # u = open('output.txt', "w")
        # u.write(f'{mi} {ma} {sr}')
        # u.close()

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
