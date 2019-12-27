import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget
from PyQt5 import QtCore


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 950, 600)
        self.setWindowTitle('Строка из файла')

        self.btn = QPushButton('Показать строку', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.setGeometry(QtCore.QRect(320, 450, 290, 70))
        self.btn.clicked.connect(self.run)

        self.ListWidget_c = QListWidget(self)
        self.ListWidget_c.setGeometry(QtCore.QRect(20, 20, 450, 400))
        self.ListWidget_c.setObjectName("listView")

        self.ListWidget_nc = QListWidget(self)
        self.ListWidget_nc.setGeometry(QtCore.QRect(475, 20, 450, 400))
        self.ListWidget_nc.setObjectName("listView")

    def run(self):
        g = list(open("lines.txt", encoding="utf-8"))
        c = []
        nc = []
        if len(g) != 0:
            for i in range(len(g)):
                if i % 2 == 0:
                    c.append(g[i])
                    print(c)
            for i in range(len(g)):
                if i % 2 != 0:
                    nc.append(g[i])
                    print(nc)
            cs = ''.join(c)
            snc = ''.join(nc)
            self.ListWidget_c.addItem(cs)
            self.ListWidget_nc.addItem(snc)
        else:
            self.ListWidget_nc.addItem('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
