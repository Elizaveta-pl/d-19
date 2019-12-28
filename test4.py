import sys

from PyQt5.QtWidgets import *
from test_project.widget import Ui_Dialog


class MainWindow(QMainWindow, Ui_Dialog):
    def __init__(self, parent=None, *args, **kwargs):
        QMainWindow.__init__(self)
        self.setupUi(self)



    # def createTable(self, columnName, rowCount, columnCount, rowHeight):
    #     # создание таблицы
    #     '''создаем строки и столбцы в таблице
    #     columnName - подписи шапки таблицы
    #     rowCount - количество строк таблицы
    #     columnCount - количество столбцов таблицы
    #     rowHeight - высота строки'''
    #
    #     # Режим растяжения таблицы по вертикали и горизонтали
    #     self.table.verticalHeader().setResizeMode(QHeaderView.Fixed)
    #     self.table.horizontalHeader().setResizeMode(QHeaderView.Stretch)
    #
    #     # Режим выделения. Выделяем только строки. Выделяем только одну строку.
    #     self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
    #     self.table.setSelectionMode(QAbstractItemView.SingleSelection)
    #
    #     # Стилизуем шапку таблицы
    #     self.table.horizontalHeader().setStyleSheet(
    #         "QHeaderView::section{font-weight:bold; color:#46647F; height:26px}");
    #
    #     # self.table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers) # Запрет редактирования таблицы
    #     self.table.setEditTriggers(QAbstractItemView.CurrentChanged)  # выделение элемента
    #     self.table.setEditTriggers(QAbstractItemView.DoubleClicked)
    #
    #     self.table.setRowCount(rowCount)  # Устанавливаем количество строк
    #     self.table.setColumnCount(columnCount)  # Устанавливаем количество столбцов
    #     # self.table.itemChanged.connect(self.edit_cell) # сохр изменений в ячейке
    #     self.table.cellChanged.connect(self.edit_cell)
    #
    #     i = 0  # формируем подписи шапки:
    #     for name in columnName:
    #         item = QTableWidgetItem()
    #         item.setText(name)
    #         self.table.setHorizontalHeaderItem(i, item)
    #         i += 1
    #
    #     # Устанавливаем высоту строк
    #     for i in range(0, rowCount):
    #         self.table.setRowHeight(i, rowHeight)
    #
    #     self.table.setColumnWidth(2, 50)
    #     # self.table.setMovement(Free)
    #     self.table.setDragDropMode(1)
    #     # self.table.itemClicked.connect(self.on_click)
    #     # self.table.itemChanged.connect(self.on_click2)
    #     # self.table.itemDoubleClicked.connect(self.on_double_click)
    #     self.db_in_tabl()
    # # ЛОГИКА

def main():
    app = QApplication(sys.argv)
    main = MainWindow()
    main.move(300, 100)  # сдвиг окна от верхнего левого угла экрана
    # main.setPalette(pal)  # передаёт изменёный цвет окну
    main.show()  # запускает окно
    app.exec()
    # sys.exit(app.exec_)

main()

