import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5 import QtCore


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Строка из файла')

        self.btn = QPushButton('Показать строку', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(100, 200)
        self.btn.clicked.connect(self.run)

        self.label = QLabel(self)
        self.label.setGeometry(QtCore.QRect(30, 100, 250, 60))
        self.label.setWordWrap(True)
        self.label.move(25, 100)

    def run(self):
        g = list(open("lines.txt", encoding="utf-8"))
        if len(g) != 0:
            d = random.randrange(0, (len(g) - 1))
            h = g[d]
            self.label.setText(h)
        else:
            self.label.setText('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
