import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtWidgets import QFrame, QVBoxLayout, QCheckBox, QPlainTextEdit
from PyQt5 import QtCore


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI(self)

    def initUI(self, Dialog):
        Dialog.resize(500, 300)

        self.btn = QPushButton(Dialog)
        self.btn.move(200, 250)
        self.btn.clicked.connect(self.check)

        self.check = QPlainTextEdit(Dialog)
        self.check.setGeometry(QtCore.QRect(280, 25, 200, 200))
        self.check.setObjectName("check")
        self.check.raise_()

        self.label = QLabel('Чек:', Dialog)
        self.label.setGeometry(QtCore.QRect(280, 5, 50, 20))

        self.cheez_burger = QCheckBox(self)
        self.cheez_burger.setObjectName('Чизбургер')
        self.cheez_burger.move(20, 20)

        self.gamburger = QCheckBox(self)
        self.gamburger.setObjectName('Гамбургер')
        self.gamburger.move(20, 50)

        self.fri = QCheckBox(self)
        self.fri.setObjectName('Картофель Фри')
        self.fri.move(20, 80)

        self.tea = QCheckBox(self)
        self.tea.setObjectName('Чай')
        self.tea.move(170, 20)

        self.coffee = QCheckBox(self)
        self.coffee.setObjectName('Кофе')
        self.coffee.move(170, 50)

        self.colla = QCheckBox(self)
        self.colla.setObjectName('Кока-Кола')
        self.colla.move(170, 80)

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

    def check(self):
        self.check.clear()
        for button in self.findChildren(QCheckBox):
            if button.isChecked():
                print(button.isChecked())
                self.check.appendPlainText(button.objectName())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
