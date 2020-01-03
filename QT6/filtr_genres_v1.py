from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.ganr = {"комедия": '1', "драма": '2', "мелодрама": '3', "детектив": '4', "документальный": '5',
                     "ужасы": '6', "музыка": '7', "фантастика": '8', "анимация": '9', "биография": '10', "боевик": '11',
                     "приключения": '13', "война": '15', "семейный": '16', "триллер": '17',
                     "фэнтези": '18', "вестерн": '19', "мистика": '20', "короткометражный": '21', "мюзикл": '22',
                     "исторический": '23', "нуар": '24'}
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(617, 506)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.tableWidget = QtWidgets.QTableView(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 60, 611, 401))
        self.tableWidget.setObjectName("tableView")

        self.pushButton = QtWidgets.QPushButton(MainWindow)
        self.pushButton.setGeometry(QtCore.QRect(250, 475, 200, 21))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.filtr)

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(410, 20, 181, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems(["комедия", "драма", "мелодрама", "детектив", "документальный",
                     "ужасы", "музыка", "фантастика", "анимация", "биография", "боевик",
                     "приключения", "война", "семейный", "триллер",
                     "фэнтези", "вестерн", "мистика", "короткометражный", "мюзикл",
                     "исторический", "нуар"])

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 617, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def genres(self):


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Фильтрация по жанрам"))

    def filtr(self):
        self.tableWidget.clear()

        labels = ['Сумма', 'Операция', 'День', 'Месяц']

        self.tableWidget.setColumnCount(len(labels))
        self.tableWidget.setHorizontalHeaderLabels(labels)
        g = self.ganr.get(self.comboBox.currentText())
        print(g)
        with sqlite3.connect("films.db") as connect:
            for id, title, year, genre, duration in connect.execute(
                    f"""SELECT * FROM Films where genre = {g}"""):
                row = self.tableWidget.rowCount()
                self.tableWidget.setRowCount(row + 1)
                self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(title)))
                self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(year)))
                self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(genre)))
                self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(duration)))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())