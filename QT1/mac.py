import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtWidgets import QFrame, QVBoxLayout, QCheckBox, QPlainTextEdit
from PyQt5 import QtCore

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI(self)

    def initUI(self, Dialog):
        # Dialog.setGeometry(100, 100, 500, 300)
        # Dialog.setWindowTitle('Макдоналдс')
        Dialog.resize(500, 300)

        self.btn = QPushButton(Dialog)
        # self.btn.resize(self.btn.sizeHint())
        self.btn.move(200, 250)
        self.btn.clicked.connect(self.check)


        self.check = QPlainTextEdit(Dialog)
        self.check.setGeometry(QtCore.QRect(280, 25, 200, 200))
        self.check.setObjectName("check")
        # self.check.setPlainText("Chek")
        self.check.raise_()

        self.label = QLabel('Чек:', Dialog)
        self.label.setGeometry(QtCore.QRect(280, 5, 50, 20))
        # self.centerLyt.addWidget(label)

        self.cheez_burger = QCheckBox("Чизбургер", self)
        self.cheez_burger.setObjectName('Чизбургер')
        self.cheez_burger.move(20, 20)

        self.gamburger = QCheckBox("Гамбургер1", self)
        self.gamburger.setObjectName('Гамбургер')
        self.gamburger.move(20, 50)

        self.fri = QCheckBox("Картофель Фри", self)
        self.fri.move(20, 80)

        self.tea = QCheckBox("Чай", self)
        self.tea.move(170, 20)

        self.coffee = QCheckBox("Кофе", self)
        self.coffee.move(170, 50)

        self.colla = QCheckBox("Кока-Кола", self)
        self.colla.move(170, 80)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.show()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Макдоналдс"))
        self.btn.setText(_translate("Dialog", "Заказать"))
        self.gamburger.setText(_translate("Dialog", "Гамбургер"))


    def check(self):
        if self.cheez_burger.isChecked():
            text = self.cheez_burger.text()
            print(f'text = {text}')
            # self.check.setPlainText(text)

        for button in self.findChildren(QCheckBox):
            if button.isChecked():
                self.check.setPlainText(button.objectName())
            print(button.isChecked())
            print(button)
            print(button.objectName())
            # button.clicked.connect(_on_button_clicked)
        # chislo = int(self.chislo_input.text())
        # chislo2 = int(self.chislo2_input.text())
        # print(chislo)
        # if chislo2 == 0:
        #     self.label_error.setText("На 0 делить нельзя. Измените 2 число.")
        # else:
        #     self.LCD_delen.display(chislo // chislo2)
        # self.LCD_plus.display(chislo + chislo2)
        # self.LCD_minus.display(chislo - chislo2)
        # self.LCD_umn.display(chislo * chislo2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())