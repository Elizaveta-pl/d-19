# Python 3. PyQt5
# -*- coding: utf-8 -*-
import sys
import pickle
from PyQt5 import QtGui, QtCore, QtWidgets

# ЦВЕТА ПОЛЕЙ
sss_vivod = ("background-color: #456173; color: #f2f2f0; font: 10pt 'Courier New'")
sss = ("background-color: #456173; color: #f2f2f0; font: 10pt 'Arial'")
columnName = ["Первый", "Второй", "Третий", "Четвёртый"]  # заголовки табл
# db_tb = [] # Будущая структура данных
rowCount = 1  # число строк
rowHeight = 20  # высота строки
columnCount = 4  # число столбцов
stb = ['stb_1', 'stb_2', 'stb_3', 'stb_4']


# ГРАФИКА
class Window(QtWidgets):  # Класс Window  наследует класс QWidget
    def __init__(self, parent=None):  # Создаёт конструктор класса, parent - ссылка на родительский эл-т
        QtWidgets.__init__(self, parent)
        super().__init__(parent, QtCore.Qt.Window)

        self.setMinimumSize(400, 600)  # Ширина и высота окна
        self.resize(600, 800)  # шир / выс окна
        self.setWindowTitle('Возможности таблицы QTableWidget')  # Заголовок
        self.setWindowIcon(QtGui.QIcon('icon.png'))  # Иконка
        # Рисуем таблицу
        self.table = QtWidgets.QTableWidget()
        self.createTable(columnName, rowCount, columnCount, rowHeight)
        # БЛОК РАЗМЕТКИ
        self.vbox_os = QtGui.QVBoxLayout()  # Создали объект вертикальный контейнер
        self.grid = QtGui.QGridLayout()  # создание сетки
        self.grid.setSpacing(5)
        # >>> ИСХОДНЫЕ ДАННЫЕ
        self.pole_1 = QtGui.QLineEdit('')
        self.pole_1.setStyleSheet(sss)
        self.grid.addWidget(self.pole_1, 0, 0)
        # ---
        self.pole_2 = QtGui.QLineEdit('')
        self.pole_2.setStyleSheet(sss)
        self.grid.addWidget(self.pole_2, 0, 1)
        # ---
        self.pole_3 = QtGui.QLineEdit('')
        self.pole_3.setStyleSheet(sss)
        self.grid.addWidget(self.pole_3, 0, 2)
        # ---
        self.pole_4 = QtGui.QLineEdit('')
        self.pole_4.setStyleSheet(sss)
        self.grid.addWidget(self.pole_4, 0, 3)
        # ---
        self.button_prnt = QtGui.QPushButton('Принт ДБ')
        self.button_prnt.clicked.connect(self.on_prnt)
        self.grid.addWidget(self.button_prnt, 1, 0)
        # ---
        self.button_add = QtGui.QPushButton('Добавить в табл.')
        self.button_add.clicked.connect(self.on_button_add)
        self.grid.addWidget(self.button_add, 1, 1)
        # ---
        self.button_del_row = QtGui.QPushButton('Удалить стр')
        self.button_del_row.clicked.connect(self.on_del_row)
        self.grid.addWidget(self.button_del_row, 1, 2)
        # --- ---
        self.button_edit_row = QtGui.QPushButton('Редактировать стр')
        self.button_edit_row.clicked.connect(self.on_edit_row)
        self.grid.addWidget(self.button_edit_row, 2, 0)
        # ---
        self.button_save_row = QtGui.QPushButton('Сохранить стр')
        self.button_save_row.clicked.connect(self.on_save_row)
        self.grid.addWidget(self.button_save_row, 2, 1)
        # ---
        self.button_up_row = QtGui.QPushButton('Вверх стр')
        self.button_up_row.clicked.connect(self.on_up_row)
        self.grid.addWidget(self.button_up_row, 2, 2)
        # ---
        self.button_down_row = QtGui.QPushButton('Вниз стр')
        self.button_down_row.clicked.connect(self.on_down_row)
        self.grid.addWidget(self.button_down_row, 2, 3)
        self.polya = [self.pole_1, self.pole_2, self.pole_3, self.pole_4]
        # >>> КОНЕЦ: ИСХОДНЫЕ ДАННЫЕ

        self.vbox_os.addLayout(self.grid)
        self.vbox_os.addWidget(self.table)  # Таблица 1
        # ---
        self.pole_vivod = QtGui.QTextEdit('')
        self.pole_vivod.setStyleSheet(sss_vivod)
        self.vbox_os.addWidget(self.pole_vivod)
        # ---
        self.setLayout(self.vbox_os)  # установка рабочей области

    def createTable(self, columnName, rowCount, columnCount, rowHeight):
        # создание таблицы
        '''создаем строки и столбцы в таблице
        columnName - подписи шапки таблицы
        rowCount - количество строк таблицы
        columnCount - количество столбцов таблицы
        rowHeight - высота строки'''

        # Режим растяжения таблицы по вертикали и горизонтали
        self.table.verticalHeader().setResizeMode(QtGui.QHeaderView.Fixed)
        self.table.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)

        # Режим выделения. Выделяем только строки. Выделяем только одну строку.
        self.table.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.table.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)

        # Стилизуем шапку таблицы
        self.table.horizontalHeader().setStyleSheet(
            "QHeaderView::section{font-weight:bold; color:#46647F; height:26px}");

        # self.table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers) # Запрет редактирования таблицы
        self.table.setEditTriggers(QtGui.QAbstractItemView.CurrentChanged)  # выделение элемента
        self.table.setEditTriggers(QtGui.QAbstractItemView.DoubleClicked)

        self.table.setRowCount(rowCount)  # Устанавливаем количество строк
        self.table.setColumnCount(columnCount)  # Устанавливаем количество столбцов
        # self.table.itemChanged.connect(self.edit_cell) # сохр изменений в ячейке
        self.table.cellChanged.connect(self.edit_cell)

        i = 0  # формируем подписи шапки:
        for name in columnName:
            item = QtGui.QTableWidgetItem()
            item.setText(name)
            self.table.setHorizontalHeaderItem(i, item)
            i += 1

        # Устанавливаем высоту строк
        for i in range(0, rowCount):
            self.table.setRowHeight(i, rowHeight)

        self.table.setColumnWidth(2, 50)
        # self.table.setMovement(Free)
        self.table.setDragDropMode(1)
        # self.table.itemClicked.connect(self.on_click)
        # self.table.itemChanged.connect(self.on_click2)
        # self.table.itemDoubleClicked.connect(self.on_double_click)
        self.db_in_tabl()

    # ЛОГИКА

    def on_start(self):
        pass

    def on_button_add(self):  # кнопка добавления
        # сбор данных для 1 строки
        db_tb_i = dict(stb_1=self.pole_1.text(),
                       stb_2=self.pole_2.text(),
                       stb_3=self.pole_3.text(),
                       stb_4=self.pole_4.text())
        # конец: сбор данных
        db_tb = self.read_data_file()  # Читаем исходный файл
        db_tb.append(db_tb_i)  # данные для новой строки табл
        self.add_in_file(db_tb)  # Записываем в файл ИД
        self.change_table(db_tb)  # В таблицу вставляем значения
        Window.on_clear(self)  # очищаем поля

    def click_btn_Read(self):  # кнопка прочитать базу из файла и вставить в табл
        text = self.read_data_file()
        self.change_table(text)  # изменить таблицу

    def on_clear(self):  # очистить поля ввода
        for i in range(0, len(self.polya)):
            self.polya[i].clear()
        '''self.pole_1.clear()
        self.pole_2.clear()
        self.pole_3.clear()
        self.pole_4.clear()'''

    def add_in_file(self, db_tb):
        # добавление в файл данных и их возврат в вызывющую функцию
        with open('database3.db', 'wb') as f:
            pickle.dump(db_tb, f)

    def read_data_file(self):  # чтение данных из файла БД
        # Чтение из файла, если его не существует, то создаем его
        try:
            with open('database3.db', 'rb') as f:  # пытаемся открыть файл
                try:
                    return pickle.load(f)  # возвращаем содержимое файла
                except EOFError:  # если файл пустой
                    return []  # возвращаем пустой список

        except FileNotFoundError:  # если файл не существует
            f = open('database3.db', 'wb')
            f.close()
            return []  # в файле нет данных

    def change_table(self, text):
        for i in range(1, len(text) + 1):
            if len(text) >= rowCount:  # если не хватает строк
                self.table.setRowCount(i)  # добавить строку
                self.table.setRowHeight(i - 1, rowHeight)

            item1 = QtGui.QTableWidgetItem()
            item1.setText(text[i - 1]['stb_1'])  # имя - ключ столбца
            self.table.setItem(i - 1, 0, item1)
            # self.table.horizontalHeader().setResizeMode(0, QtGui.QHeaderView.ResizeToContents)

            item2 = QtGui.QTableWidgetItem()
            item2.setText(text[i - 1]['stb_2'])
            self.table.setItem(i - 1, 1, item2)
            # self.table.horizontalHeader().setResizeMode(1, QtGui.QHeaderView.ResizeToContents)
            item3 = QtGui.QTableWidgetItem()
            item3.setText(text[i - 1]['stb_3'])
            self.table.setItem(i - 1, 2, item3)
            # self.table.horizontalHeader().setResizeMode(1, QtGui.QHeaderView.ResizeToContents)
            item4 = QtGui.QTableWidgetItem()
            item4.setText(text[i - 1]['stb_4'])
            self.table.setItem(i - 1, 3, item4)
            # self.table.horizontalHeader().setResizeMode(1, QtGui.QHeaderView.ResizeToContents)

    def edit_cell(self):  # изменение данных ячейки
        print('edit_cell =')

    '''def on_up_row (self): # перемещение строки вверх
        row_index = self.table.currentRow()
        if row_index == 0:
            pass
        else:
            pass'''

    def on_up_row(self):  # перемещение строки вверх
        row_index = self.table.currentRow()
        if row_index == 0:
            pass
        else:
            db_tb = self.read_data_file()
            db_tb.insert(row_index - 1, db_tb[row_index])
            del db_tb[row_index + 1]
            self.add_in_file(db_tb)
            # self.change_table(db_tb) # В таблицу вставляем значения
            self.table.insertRow(row_index - 1)
            # self.table.selectRow(row_index-1)

    def on_down_row(self):  # перемещение строки вниз
        row_index = self.table.currentRow()
        db_tb = self.read_data_file()
        if row_index + 1 == len(db_tb):
            pass
        else:
            self.add_in_file(db_tb)
            db_tb.insert(row_index + 2, db_tb[row_index])
            del db_tb[row_index]
            self.add_in_file(db_tb)
            self.change_table(db_tb)  # В таблицу вставляем значения
            self.table.selectRow(row_index + 1)  # выделяет передвинутую строку

    def db_in_tabl(self):  # вставить базу данных в таблицу
        text = self.read_data_file()
        self.change_table(text)

    def on_del_row(self):
        db_tb = self.read_data_file()
        row_index = self.table.currentRow()
        # db_tb.pop(row_index)
        del db_tb[row_index]
        self.table.removeRow(row_index)
        self.add_in_file(db_tb)

    def on_edit_row(self):  # правка строки в полях ввода
        row_index = self.table.currentRow()
        db_tb = self.read_data_file()
        db_tb_i = db_tb[row_index]

        for i in range(0, len(self.polya)):
            self.polya[i].setText(db_tb_i[stb[i]])

    def on_save_row(self):
        # сбор данных для 1 строки
        db_tb_i = dict(stb_1=self.pole_1.text(),
                       stb_2=self.pole_2.text(),
                       stb_3=self.pole_3.text(),
                       stb_4=self.pole_4.text())
        # конец: сбор данных

        db_tb = self.read_data_file()
        row_index = self.table.currentRow()
        db_tb.pop(row_index)
        db_tb.insert(row_index, db_tb_i)
        self.add_in_file(db_tb)
        self.change_table(db_tb)  # В таблицу вставляем значения
        self.on_clear()

    def on_prnt(self):
        db_tb = self.read_data_file()
        for i in range(0, len(db_tb)):
            print(i, ':', db_tb[i], sep='')


# КОНЕЦ
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Window()  # создаёт экземпляр окна из класса
    window.move(40, 20)  # сдвиг окна от верхнего левого угла экрана
    pal = window.palette()
    pal.setBrush(QtGui.QPalette.Window, QtGui.QBrush(QtGui.QColor("#222831")))
    window.setPalette(pal)  # передаёт изменёный цвет окну
    window.show()  # запускает окно
    sys.exit(app.exec_())