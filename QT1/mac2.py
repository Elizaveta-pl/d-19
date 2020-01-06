import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtWidgets import QSpinBox, QTableWidget, QCheckBox, QPlainTextEdit
from PyQt5 import QtCore


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI(self)

    def initUI(self, Dialog):
        Dialog.resize(640, 300)
        # Создаем словарь с наименованиями блюд, ценами и количеством в заказе
        self.menu = {'Чизбургер': [20, 0], 'Гамбургер': [30, 0],
                     'Картофель Фри': [40, 0], 'Чай': [5, 0],
                     'Кофе': [10, 0], 'Кока-Кола': [13, 0]}
        # Из ключей словаря menu формируем список блюд
        self.menu3 = list(self.menu.keys())
        self.menu1 = []
        self.menu2 = []
        # Формируем список переменных для создания QCheckBox
        self.checks = ['check' + str(i) for i in range(len(self.menu))]
        # Формируем список переменных для создания  QSpinBox
        self.spins = ['spin' + str(i) for i in range(len(self.menu))]

        # создаём экземпляр класса QPushButton
        self.btn = QPushButton(Dialog)
        # задаём размер кнопки
        self.btn.move(200, 250)
        #  Указываем действие при нажатии на кнопку
        self.btn.clicked.connect(self.check)
        # создаём экземпляр класса QPlainTextEdit
        self.check = QPlainTextEdit(Dialog)
        self.check.setGeometry(QtCore.QRect(260, 25, 350, 200))
        self.check.setObjectName("check")
        self.check.raise_()
        # создаём экземпляр класса QLabel
        self.label = QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(260, 5, 50, 20))

        # Создаем элеметы QCheckBox и QSpinBox
        for i in range(len(self.menu)):
            # print(f' name1 = {list(self.menu.keys())[i]}')
            self.add_element(list(self.menu.keys())[i], i)

        self.check_tab = QWidget()
        self.check_tab.setObjectName("check")

        # self.checkWidget = QTableWidget(Dialog)
        # self.checkWidget.setGeometry(QtCore.QRect(530, 25, 256, 151))
        # self.checkWidget.setObjectName("checkWidget")
        # self.checkWidget.setColumnCount(0)
        # self.checkWidget.setRowCount(0)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.show()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Макдоналдс"))
        self.btn.setText(_translate("Dialog", "Заказать"))
        self.label.setText(_translate("Dialog", "Чек:"))

        name = self.menu.keys()
        print(f' name = {list(name)[0]}')
        print(f' len = {len(self.menu)}')
        # for i in range(len(self.menu)):
        #     print(f' name = {list( self.menu.keys())[i]}')
        #     name = f'self.check_{i}'
        #     print(type(self.check_0))
        print(dir(self))
        # print(f'name {name.setText(_translate("Dialog", list( self.menu.keys())[i]))}')
        # self.f"self.check_{i}".setText(_translate("Dialog", list( self.menu.keys())[i]))

    def change(self, name, value):
        print(f'name_check = {name}, value = {value}')
        # self.r = int(self.spin_cheez_burger.text())
        # # Price
        # print(f'self.r = {self.r}')
        # for i in self.menu.keys():
        #     print(f'i = {i}')
        # print(f'self.check1.objectName()= {self.checks[0].objectName()}')
        # dir()

    def check(self):
        self.check.clear()
        itogo = 0
        # Перебираем все обекты QCheckBox
        for button in self.findChildren(QCheckBox):
            # Если QCheckBox выбран выводим на печать

            if button.isChecked():
                # print(button.isChecked())
                index = self.menu3.index(button.objectName())
                stoimost = self.menu[button.objectName()][0]\
                           * self.spins[index].value()
                itogo = itogo + stoimost

                print(
                    f'Имя = {button.objectName()} '
                    f' количество  {self.spins[index].value()}'
                    f' цена {self.menu[button.objectName()][0]}'
                    f' стоимость {stoimost}')
                print_check = f'{button.objectName()} - ' \
                              f'{self.spins[index].value()} ' \
                              f'- {self.menu[button.objectName()][0]}' \
                              f' - {stoimost}'
                self.check.appendPlainText(print_check)
        self.check.appendPlainText(str(itogo))

    def state_changed(self, name):
        index = self.menu3.index(name)
        print(f'state_changed = {name}')
        print(f'checks = {self.checks[index].objectName()}')
        print(f'spins = {self.spins[index].objectName()}')
        print(f'index = {index}')

        if self.checks[index].isChecked():
            # При выборе блюда, количество устанавливаем равным 1.
            self.spins[index].setValue(1)
        else:
            # При отказе от блюда, количество устанавливаем равным 0.
            self.spins[index].setValue(0)

        # if self.cheez_burger.isChecked():
        #    self.label.setText("CHECKED!")
        #    self.spin_cheez_burger.setValue(1)
        #    # self.spin_cheez_burger.text() == 1
        #    self.change
        # else:
        #    self.spin_cheez_burger.setValue(0)
        #    self.label.setText("UNCHECKED!")

    def add_element(self, name, int):
        _translate = QtCore.QCoreApplication.translate
        y = 20 + (int + 1) * 25
        # создаём экземпляр класса QCheckBox
        self.checks[int] = QCheckBox(self)
        self.checks[int].setObjectName(str(name))
        self.checks[int].stateChanged.connect(lambda: self.state_changed(name))
        self.checks[int].move(20, y)
        self.checks[int].setText(_translate("Dialog", str(name)))

        # self.menu1.append(self.checks[int].objectName())
        # print(f'menu1 = {self.menu1}')

        # создаём экземпляр класса QSpinBox
        self.spins[int] = QSpinBox(self)
        self.spins[int].setGeometry(QtCore.QRect(170, y, 40, 22))
        self.spins[int].setObjectName(str(name))
        self.spins[int].valueChanged.connect(
            lambda: self.change(name, self.spins[int].value()))

        # self.menu2.append(self.spins[int].objectName())
        # print(f'menu2 = {self.menu2}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
