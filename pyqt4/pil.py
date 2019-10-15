from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QPushButton, QLineEdit,QLabel
from PyQt5.QtGui import QPixmap
import sys
from PIL import Image

SCREEN_SIZE = [400, 400]

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 400, *SCREEN_SIZE)
        self.setWindowTitle('Отображение картинки')

        self.pixmap = QPixmap('image.png.jpg')
        self.image = QLabel(self)
        self.image.move(80, 60)
        self.image.resize(250, 250)
        #self.mirror()
        self.image.setPixmap(self.pixmap)

    # def mirror(self):
    #     self.pixmap.transpose(Image.FLIP_TOP_BOTTOM)
    #     self.pixmap.transpose(Image.ROTATE_90)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())