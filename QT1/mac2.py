import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtWidgets import QSpinBox, QCheckBox, QPlainTextEdit
from PyQt5 import QtCore


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI(self)

    def initUI(self, Dialog):
        Dialog.resize(640, 300)
        # Создаем словарь с наименованиями блюд, ценами
        self.menu = {'Чизбургер': 20, 'Гамбургер': 30,
                     'Картофель Фри': 40, 'Чай': 5,
                     'Кофе': 10, 'Кока-Кола': 13}
        # Из ключей словаря menu формируем список блюд
        self.menu3 = list(self.menu.keys())

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
            self.add_element(list(self.menu.keys())[i], i)

        self.check_tab = QWidget()
        self.check_tab.setObjectName("check")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.show()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Макдоналдс"))
        self.btn.setText(_translate("Dialog", "Заказать"))
        self.label.setText(_translate("Dialog", "Чек:"))
        name = self.menu.keys()

    def change(self, name, value):
        pass


    def check(self):
        self.check.clear()
        itogo = 0
        # Перебираем все обекты QCheckBox
        for button in self.findChildren(QCheckBox):
            # Если QCheckBox выбран выводим на печать

            if button.isChecked():
                # print(button.isChecked())
                index = self.menu3.index(button.objectName())
                stoimost = self.menu.get(button.objectName()) \
                           * self.spins[index].value()
                itogo = itogo + stoimost
                print_check_name = f'{button.objectName()}'
                print_cek_sum = f' {self.spins[index].value()}' \
                                f'- {self.menu.get(button.objectName())}' \
                                f' - {stoimost}'
                print_check = print_check_name.ljust(30) + '\t \t' + print_cek_sum

                self.check.appendPlainText(print_check)
        self.check.appendPlainText(f'\n \t \t \tИтого: {itogo}'.rjust(20))

    def state_changed(self, name):
        index = self.menu3.index(name)

        if self.checks[index].isChecked():
            # При выборе блюда, количество устанавливаем равным 1.
            self.spins[index].setValue(1)
        else:
            # При отказе от блюда, количество устанавливаем равным 0.
            self.spins[index].setValue(0)


    def add_element(self, name, int):
        _translate = QtCore.QCoreApplication.translate
        y = 20 + (int + 1) * 25
        # создаём экземпляр класса QCheckBox
        self.checks[int] = QCheckBox(self)
        self.checks[int].setObjectName(str(name))
        self.checks[int].stateChanged.connect(lambda: self.state_changed(name))
        self.checks[int].move(20, y)
        self.checks[int].setText(_translate("Dialog", str(name)))

        # создаём экземпляр класса QSpinBox
        self.spins[int] = QSpinBox(self)
        self.spins[int].setGeometry(QtCore.QRect(170, y, 40, 22))
        self.spins[int].setObjectName(str(name))
        self.spins[int].valueChanged.connect(
            lambda: self.change(name, self.spins[int].value()))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
