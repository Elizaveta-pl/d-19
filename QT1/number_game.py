import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtWidgets import QLCDNumber


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def random_number(self):
        self.x = round(random.randint(0, 100), 2)
        self.y = round(random.randint(0, 100), 2)
        self.z = round(random.randint(0, 100), 2)
        self.step = 10

    def initUI(self):
        self.random_number()
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Числовая игра')

        self.btn = QPushButton('Увеличить', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(50, 210)
        self.btn.clicked.connect(self.plus)

        self.btn = QPushButton('Уменьшить', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(150, 210)
        self.btn.clicked.connect(self.minus)

        self.label = QLabel(self)
        self.label.setText("Осталось ходов")
        self.label.move(20, 20)

        self.LCD_step = QLCDNumber(self)
        self.LCD_step.move(140, 10)
        self.LCD_step.resize(80, 40)
        self.LCD_step.display(self.step)

        self.LCD_x = QLCDNumber(self)
        self.LCD_x.move(60, 100)
        self.LCD_x.resize(160, 100)
        self.LCD_x.display(self.x)

        self.label_er = QLabel(self)
        self.label_er.setText(f'                                                                 '
                              f'                                          ')
        self.label_er.move(5, 60)

        self.label_er1 = QLabel(self)
        self.label_er1.setText(f'                                                                 ')
        self.label_er1.move(5, 70)

    def plus(self):
        self.x = self.x + self.y
        self.label_er.setText(f'                                                         '
                              f'                                                          ')
        self.label_er1.setText(f'                                                         ')
        self.count()
        self.LCD_x.display(self.x)
        pass

    def minus(self):
        self.x = self.x - self.z
        self.label_er.setText(f'                                                         '
                              f'                                                          ')
        self.label_er1.setText(f'                                                         ')
        self.count()
        self.LCD_x.display(self.x)

    def count(self):
        if self.x == 0:
            self.label_er.setText(f'Поздравляю, вы победили!')
        else:
            if self.step == 1:
                self.label_er.setText(f'Ходы закончились, нажмите кнопку для того,\n')
                self.label_er1.setText(f'что бы начать заново.')
                self.LCD_step.display(0)
                self.x = round(random.randint(0, 100), 2)
                self.random_number()

            else:
                self.step -= 1
                self.label.setText(f'Осталось ходов {self.step}')
                self.LCD_step.display(self.step)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
