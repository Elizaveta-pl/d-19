# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test1.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from time import time

# from test_project.rashod import Rashod
# from test_project.edit import Edit


columnName = ["Первый", "Второй", "Третий", "Четвёртый"] # заголовки табл
# db_tb = [] # Будущая структура данных
rowCount = 1 # число строк
rowHeight = 20 # высота строки
columnCount = 4 # число столбцов
stb = ['stb_1','stb_2','stb_3','stb_4']
import sqlite3


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Dialog)
        self.centralwidget.setObjectName("centralwidget")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setGeometry(QtCore.QRect(8, 560, 782, 26))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.lcdNumPostOst = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumPostOst.setGeometry(QtCore.QRect(710, 85, 80, 23))
        self.lcdNumPostOst.setObjectName("lcdNumPostOst")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QtCore.QRect(710, 59, 80, 20))
        self.label_2.setMinimumSize(QtCore.QSize(80, 20))
        self.label_2.setMaximumSize(QtCore.QSize(80, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(8, 114, 696, 440))
        self.tabWidget.setObjectName("tabWidget")
        self.Post = QtWidgets.QWidget()
        self.Post.setObjectName("Post")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.Post)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.tablePostupl = QtWidgets.QTableWidget(self.Post)
        self.tablePostupl.setObjectName("tablePostupl")
        self.tablePostupl.setColumnCount(0)
        self.tablePostupl.setRowCount(0)

        self.gridLayout_2.addWidget(self.tablePostupl, 0, 0, 1, 1)
        self.tabWidget.addTab(self.Post, "")
        self.rashod = QtWidgets.QWidget()
        self.rashod.setObjectName("rashod")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.rashod)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tableRashod = QtWidgets.QTableView(self.rashod)
        self.tableRashod.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tableRashod.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.tableRashod.setAcceptDrops(False)
        self.tableRashod.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.tableRashod.setGridStyle(QtCore.Qt.SolidLine)
        self.tableRashod.setObjectName("tableRashod")

        # Рисуем таблицу
        # self.tableRashod = QtGui.QTableWidget()
        tablename = self.tablePostupl
        # tablename = "tableRashod"
        self.createTable(tablename, columnName, rowCount, columnCount, rowHeight)

        self.gridLayout_3.addWidget(self.tableRashod, 0, 0, 1, 1)
        self.tabWidget.addTab(self.rashod, "")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(710, 4, 80, 20))
        self.label.setMaximumSize(QtCore.QSize(80, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lcdNumPost = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumPost.setGeometry(QtCore.QRect(710, 30, 80, 23))
        self.lcdNumPost.setObjectName("lcdNumPost")

        # Добавляем кнопки для редактирования
        # self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        # self.toolButton.setGeometry(QtCore.QRect(730, 180, 26, 24))
        # self.toolButton.setObjectName("toolButton")
        self.bottonAdd = QtWidgets.QPushButton(self.centralwidget)
        self.bottonAdd.setGeometry(QtCore.QRect(720, 270, 41, 25))
        self.bottonAdd.setObjectName("bottonAdd")
        self.bottonAdd.clicked.connect(self.add_iten)
        self.bottonEdit = QtWidgets.QPushButton(self.centralwidget)
        self.bottonEdit.setGeometry(QtCore.QRect(720, 300, 41, 25))
        self.bottonEdit.setObjectName("bottonEdit")
        self.bottonEdit.clicked.connect(self.edit_selec_iten)

        # QMainWindow, QPushButton, QApplication

        # self.bottonEdit.QMainWindow.clicked.connect(self.edit_selec_iten)


        Dialog.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(Dialog)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 832, 22))
        self.menubar.setObjectName("menubar")
        Dialog.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Dialog)
        self.statusbar.setObjectName("statusbar")
        Dialog.setStatusBar(self.statusbar)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)



    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Домашняя бухгалтерия"))
        self.label_2.setText(_translate("Dialog", "Остаток"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Post), _translate("Dialog", "Поступления"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.rashod), _translate("Dialog", "Расход"))
        self.label.setText(_translate("Dialog", "Остаток"))
        # self.toolButton.setText(_translate("Dialog", "..."))
        self.bottonAdd.setText(_translate("Dialog", "add"))
        self.bottonEdit.setText(_translate("Dialog", "edit"))

    def createTable(self, tableName, columnName, rowCount, columnCount, rowHeight):
        # создание таблицы
        '''создаем строки и столбцы в таблице
        columnName - подписи шапки таблицы
        rowCount - количество строк таблицы
        columnCount - количество столбцов таблицы
        rowHeight - высота строки'''
        print(tableName)
        # Режим растяжения таблицы по вертикали и горизонтали
        # self.tablePostupl.verticalHeader().setResizeMode(QtGui.QHeaderView.Fixed)
        # self.tablePostupl.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)


        # Стилизуем шапку таблицы
        tableName.horizontalHeader().setStyleSheet(
            "QHeaderView::section{font-weight:bold; color:#46647F; height:26px}");

        # Режим выделения. Выделяем только строки. Выделяем только одну строку.
        tableName.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        tableName.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)

        # блокируем редактирование таблицы
        tableName.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers) # Запрет редактирования таблицы
        # self.tablePostupl.setEditTriggers(QtWidgets.QAbstractItemView.CurrentChanged)  # выделение элемента
        # self.tablePostupl.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked)

        labels = ['Сумма', 'Операция', 'День', 'Месяц', 'Год', 'slag']

        tableName.setColumnCount(len(labels))
        tableName.setHorizontalHeaderLabels(labels)

        tableName.selectRow(rowCount)  # Устанавливаем количество строк
        # self.tablePostupl.setColumnCount(columnCount)  # Устанавливаем количество столбцов
        # self.table.itemChanged.connect(self.edit_cell) # сохр изменений в ячейке
        # self.tablePostupl.cellChanged.connect(self.edit_cell)

        # i = 0  # формируем подписи шапки:
        # for name in columnName:
        #     item = QtWidgets.QTableWidgetItem()
        #     item.setText(name)
        #     # self.tableRashod.setHorizontalHeader(i, item)
        #     i += 1

        # # Устанавливаем высоту строк
        # for i in range(0, rowCount):
        #     self.tablePostupl.setRowHeight(i, rowHeight)
        #
        # self.tablePostupl.setColumnWidth(2, 50)
        # # self.table.setMovement(Free)
        # self.tablePostupl.setDragDropMode(1)
        # # self.table.itemClicked.connect(self.on_click)
        # # self.table.itemChanged.connect(self.on_click2)
        # # self.table.itemDoubleClicked.connect(self.on_double_click)
        # # self.db_in_tabl()

        with sqlite3.connect("baza.db") as connect:
            # for  summa, operacia, day, month, year, transact, slag in connect.execute(f"""SELECT * FROM Dohodi where transact=0 ORDER BY slag"""):
            for summa, operacia, day, month, year, slag in connect.execute(
                        f"""SELECT * FROM Dohodi where transact=0 ORDER BY slag"""):
                row = self.tablePostupl.rowCount()
                tableName.setRowCount(row + 1)
                tableName.setItem(row, 0, QtWidgets.QTableWidgetItem(str(summa)))
                tableName.setItem(row, 1, QtWidgets.QTableWidgetItem(operacia))
                tableName.setItem(row, 2, QtWidgets.QTableWidgetItem(str(day)))
                tableName.setItem(row, 3, QtWidgets.QTableWidgetItem(str(month)))
                tableName.setItem(row, 4, QtWidgets.QTableWidgetItem(str(year)))
                # tableName.setItem(row, 5, QtWidgets.QTableWidgetItem(str(slag)))

    def edit_selec_iten(self):
        try:
            selected_item = self.tablePostupl.currentRow()
            print(selected_item)
            col  = self.tablePostupl.item(selected_item, 0)
            print(col.text())
            print(str(int(time())))# self.edit()
        except Exception as e:
            print('Выбирете строку для редактирования')

    def add_iten(self):
        self.vn = QtWidgets.QVBoxLayout()
        self.Form = QtWidgets.QWidget()
        self.vnoss = Edit()
        self.vnoss.setupUi(self.Form)
        self.Form.show()

    def mousePressEvent(self, event):
        self.c.closeApp.emit()

    def smotr(self):
        self.smot = QtWidgets.QVBoxLayout()
        self.Form = QtWidgets.QWidget()
        self.rash = Rashod()
        self.rash.setupUi(self.Form)
        self.Form.show()
        # smot.exec()
        # self.setLayout(smot)

    def edit(self):
        self.vn = QtWidgets.QVBoxLayout()
        self.Form = QtWidgets.QWidget()
        self.vnoss = Edit()
        self.vnoss.setupUi(self.Form)
        self.Form.show()


    # ЛОГИКА
