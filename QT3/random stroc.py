import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel


# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.setGeometry(300, 300, 300, 300)
#         self.setWindowTitle('Строка из файла')
#
#         self.btn = QPushButton('Показать строку', self)
#         self.btn.resize(self.btn.sizeHint())
#         self.btn.move(100, 200)
#         self.btn.clicked.connect(self.run)
#
#         self.label = QLabel(self)
#         self.label.setText("                                                                     "
#                            "                                                                     ")
#         self.label.move(50, 100)
#
#     def run(self):
#         g = list(open("lines.txt"))
#         print(g)
#         if len(g) != 0:
#             d = random.randrange(0, (len(g) - 1))
#             print(d)
#             h = g[d]
#             print(h)
#             self.label.config(text=str(h))
#         else:
#             self.label.setText('awsdefghjewwedrfgtyhjsedrftyguhiok')
#         # self.label.setText("OK")
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     ex.show()
#     sys.exit(app.exec())
g = list(open("lines.txt"))
print(g)
if len(g) != 0:
    d = random.randrange(0, (len(g) - 1))
    print(d)
    h = g[d]
    print(h)