import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtWidgets import QSpinBox, QTableWidget, QCheckBox, QPlainTextEdit
from PyQt5 import QtCore


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI(self)

    def initUI(self, Dialog):
        # Dialog.resize(500, 300)
        Dialog.resize(800, 400)

        self.menu = {'Чизбургер1': 20, 'Гамбургер1': 30, 'Картофель Фри1': 40, 'Чай1': 5, 'Кофе1': 10, 'Кока-Кола1': 13}
        self.menu1 = []

        self.btn = QPushButton(Dialog)
        self.btn.move(200, 250)
        self.btn.clicked.connect(self.check)

        self.check = QPlainTextEdit(Dialog)
        self.check.setGeometry(QtCore.QRect(320, 25, 200, 200))
        self.check.setObjectName("check")
        self.check.raise_()

        self.label = QLabel('Чек:', Dialog)
        self.label.setGeometry(QtCore.QRect(320, 5, 50, 20))

        self.cheez_burger = QCheckBox(self)
        self.cheez_burger.setObjectName('Чизбургер')
        self.cheez_burger.stateChanged.connect(self.state_changed)
        self.cheez_burger.move(20, 20)

        self.spin_cheez_burger = QSpinBox(self)
        self.spin_cheez_burger.setGeometry(QtCore.QRect(170, 110, 40, 25))
        self.spin_cheez_burger.valueChanged.connect(self.change)
        self.spin_cheez_burger.setObjectName("spinBox")

        # self.check_0 = QCheckBox(self)
        # self.check_0.setObjectName('Чизбургер')
        # self.check_0.stateChanged.connect(self.state_changed)
        # self.check_0.move(20, 110)
        for i in range(len(self.menu)):
            print(f' name1 = {list(self.menu.keys())[i]}')
            name = f'self.check_{i}'
            # print(type(self.check_0))
            self.add_element(list(self.menu.keys())[i], i)


        # self.spin_0 = QSpinBox(self)
        # self.spin_0.setGeometry(QtCore.QRect(170, 20, 40, 25))
        # self.spin_0.valueChanged.connect(self.change)
        # self.spin_0.setObjectName("spinBox")

        self.gamburger = QCheckBox(self)
        self.gamburger.setObjectName('Гамбургер')
        self.gamburger.move(20, 50)

        self.fri = QCheckBox(self)
        self.fri.setObjectName('Картофель Фри')
        self.fri.move(20, 80)

        self.tea = QCheckBox(self)
        self.tea.setObjectName('Чай')
        self.tea.move(220, 20)

        self.coffee = QCheckBox(self)
        self.coffee.setObjectName('Кофе')
        self.coffee.move(220, 50)

        self.colla = QCheckBox(self)
        self.colla.setObjectName('Кока-Кола')
        self.colla.move(220, 80)

        self.check_tab = QWidget()
        self.check_tab.setObjectName("check")

        self.checkWidget = QTableWidget(Dialog)
        self.checkWidget.setGeometry(QtCore.QRect(530, 25, 256, 151))
        self.checkWidget.setObjectName("checkWidget")
        self.checkWidget.setColumnCount(0)
        self.checkWidget.setRowCount(0)


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.show()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Макдоналдс"))
        self.btn.setText(_translate("Dialog", "Заказать"))
        self.gamburger.setText(_translate("Dialog", "Гамбургер"))
        self.cheez_burger.setText(_translate("Dialog", "Чизбургер"))
        self.fri.setText(_translate("Dialog", "Картофель Фри"))
        self.tea.setText(_translate("Dialog", "Чай"))
        self.coffee.setText(_translate("Dialog", "Кофе"))
        self.colla.setText(_translate("Dialog", "Кока-Кола"))
        # self.check_0.setText(_translate("Dialog", "Чизбургер"))
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


    def change(self):
        self.r = int(self.spin_cheez_burger.text())
        # Price
        # print(self.menu['Гамбургер'])
        for i in self.menu.keys():
            print(f'i = {i}')
        dir()
    def check(self):
        self.check.clear()
        for button in self.findChildren(QCheckBox):
            if button.isChecked():
                # print(button.isChecked())

                print(f'button = {button}')
                print(dir())
                self.check.appendPlainText(button.objectName())

    def state_changed(self, name):
         print(f'name_check = {name}')
         if self.cheez_burger.isChecked():
            self.label.setText("CHECKED!")
            self.spin_cheez_burger.setValue(1)
            # self.spin_cheez_burger.text() == 1
            self.change
         else:
            self.spin_cheez_burger.setValue(0)
            self.label.setText("UNCHECKED!")

    def add_element(self, name, int):
        _translate = QtCore.QCoreApplication.translate

        name_check = f'self.check_{int}'
        name_check = f'check_{int}'
        y = 120 + (int + 1) * 25
        # name = f'check_{1}'
        print(f'name = {name_check}')
        name_check = QCheckBox(self)
        name_check.setObjectName(str(name))
        name_check.stateChanged.connect(self.state_changed)
        name_check.move(20, y)
        name_check.setText(_translate("Dialog", str(name)))
        self.menu1.append(name_check.objectName())
        # print(f'name = {dir(name1)}')
        # print(f'name1 = {name1.objectName()}')
        # print(f'name_type = {type(name1)}')
        print(f'menu1 = {self.menu1}')

        name_spin = f'self.spin_{int}'
        name_spin = QSpinBox(self)
        name_spin.setGeometry(QtCore.QRect(170, y, 40, 22))
        name_spin.valueChanged.connect(self.change)
        name_spin.setObjectName("spinBox")

        # self.check_0.setObjectName('Чизбургер')
        # self.check_0.stateChanged.connect(self.state_changed)
        # self.check_0.move(20, 110)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
