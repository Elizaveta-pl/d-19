import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtWidgets import QLCDNumber, QLineEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Миникалькулятор')

        self.btn = QPushButton('Рассчитать', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(100, 200)
        self.btn.clicked.connect(self.hello)

        self.label = QLabel(self)
        self.label.setText("Введите 1 число")
        self.label.move(10, 30)

        self.label = QLabel(self)
        self.label.setText("Введите 2 число")
        self.label.move(10, 60)

        self.chislo_input = QLineEdit(self)
        self.chislo_input.move(130, 30)

        self.chislo2_input = QLineEdit(self)
        self.chislo2_input.move(130, 60)

        self.LCD_plus = QLCDNumber(self)
        self.LCD_plus.move(10, 100)

        self.LCD_minus = QLCDNumber(self)
        self.LCD_minus.move(80, 100)

        self.LCD_delen = QLCDNumber(self)
        self.LCD_delen.move(150, 100)

        self.LCD_umn = QLCDNumber(self)
        self.LCD_umn.move(210, 100)

        self.label_error = QLabel(self)
        self.label_error.setText("")
        self.label_error.move(30, 140)
        self.label_error.resize(270, 20)

    def hello(self):
        chislo = float(self.chislo_input.text())
        chislo2 = float(self.chislo2_input.text())
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