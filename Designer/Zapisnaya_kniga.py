from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(742, 546)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.book = QtWidgets.QListWidget(self.centralwidget)
        self.book.setGeometry(QtCore.QRect(350, 10, 381, 491))
        self.book.setObjectName("book")
        self.label_name = QtWidgets.QLabel(self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(20, 60, 101, 31))
        self.label_name.setObjectName("label_name")
        self.textEdit_name = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_name.setGeometry(QtCore.QRect(150, 60, 171, 31))
        self.textEdit_name.setObjectName("textEdit_name")
        self.textEdit_number = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_number.setGeometry(QtCore.QRect(150, 110, 171, 31))
        self.textEdit_number.setObjectName("textEdit_number")
        self.label_number = QtWidgets.QLabel(self.centralwidget)
        self.label_number.setGeometry(QtCore.QRect(20, 120, 111, 16))
        self.label_number.setObjectName("label_number")
        self.vnos = QtWidgets.QPushButton(self.centralwidget)
        self.vnos.setGeometry(QtCore.QRect(30, 190, 291, 31))
        self.vnos.setObjectName("vnos")
        self.vnos.clicked.connect(self.vnesti)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 742, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Записная книжка"))
        self.label_name.setText(_translate("MainWindow", "Имя контакта"))
        self.label_number.setText(_translate("MainWindow", "Номер телефона"))
        self.vnos.setText(_translate("MainWindow", "Занести"))

    def vnesti(self):
        na = self.textEdit_name.toPlainText()
        nu = self.textEdit_number.toPlainText()
        k = f"{na}   {nu}"
        self.book.addItem(k)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
