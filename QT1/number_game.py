import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtWidgets import QLCDNumber, QLineEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def random_number(self):
        self.x = round(random.uniform(0, 100),2)
        self.y = round(random.uniform(0, 100),2)
        self.z = round(random.uniform(0, 100),2)
        self.step = 10


    def initUI(self):
        self.random_number()
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Числовая игра')

        self.btn = QPushButton('Увеличить', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(50, 200)
        self.btn.clicked.connect(self.plus)

        self.btn = QPushButton('Уменьшить', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(150, 200)
        self.btn.clicked.connect(self.minus)

        self.label = QLabel(self)
        self.label.setText("Осталось ходов")
        self.label.move(20, 20)

        self.LCD_step = QLCDNumber(self)
        self.LCD_step.move(140, 10)
        self.LCD_step.resize(80, 40)
        self.LCD_step.display(self.step)

        self.LCD_x = QLCDNumber(self)
        self.LCD_x.move(70, 80)
        self.LCD_x.resize(160, 80)
        self.LCD_x.display(self.x)

        self.label = QLabel(self)
        self.label.setText(f'Осталось ходов {self.step}')
        self.label.move(80, 50)


    def plus(self):
        self.x = self.x + self.y
        self.count()
        self.LCD_x.display(self.x)
        pass

    def minus(self):
        self.x = self.x - self.z
        self.count()
        self.LCD_x.display(self.x)

    def count(self):
        self.step -= 1
        self.label.setText(f'Осталось ходов {self.step}')
        self.LCD_step.display(self.step)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())