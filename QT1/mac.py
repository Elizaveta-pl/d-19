import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtWidgets import QFrame, QVBoxLayout, QCheckBox, QPlainTextEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 500, 300)
        self.setWindowTitle('Макдоналдс')

        self.btn = QPushButton('Заказать', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(100, 200)
        #self.btn.clicked.connect(self.hello)

        self.cheez_burger = QCheckBox("Чизбургер", self)
        self.cheez_burger.move(20, 20)

        self.gamburger = QCheckBox("Гамбургер", self)
        self.gamburger.move(20, 50)

        self.fri = QCheckBox("Картофель Фри", self)
        self.fri.move(20, 80)

        self.tea = QCheckBox("Чай", self)
        self.tea.move(170, 20)

        self.coffee = QCheckBox("Кофе", self)
        self.coffee.move(170, 50)

        self.colla = QCheckBox("Кока-Кола", self)
        self.colla.move(170, 80)

        self.centerFrm = QFrame(self)
        # self.centerFrm.logicalDpiX()
        # self.centerFrm.setStyleSheet("QWidget { background-color: #ddeeff; }")

        self.centerLyt = QVBoxLayout()
        label = QLabel('Чек:')
        self.centerLyt.addWidget(label)



        self.centerFrm.setLayout(self.centerLyt)
        # self.setCentralWidget(self.centerFrm)
        #
        self.check = QPlainTextEdit()
        # self.check.setPlainText("Chek")
        # self.check.setStyleSheet("QPlainTextEdit { background-color: #ffffff; }")
        self.check.setMinimumHeight(100)
        self.check.setMaximumHeight(300)
        self.check.setMinimumWidth(100)
        self.check.setMaximumWidth(300)
        self.centerLyt.addWidget(self.check)
        self.show()

    def hello(self):
        chislo = int(self.chislo_input.text())
        chislo2 = int(self.chislo2_input.text())
        print(chislo)
        if chislo2 == 0:
            self.label_error.setText("На 0 делить нельзя. Измените 2 число.")
        else:
            self.LCD_delen.display(chislo // chislo2)
        self.LCD_plus.display(chislo + chislo2)
        self.LCD_minus.display(chislo - chislo2)
        self.LCD_umn.display(chislo * chislo2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())