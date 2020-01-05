from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtGui import QPainter, QPen, QColor, QFont, QPixmap
from PyQt5.QtCore import Qt, QPoint, pyqtSignal, QRect
import sys


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.mModified = True
        self.initUI()
        self.currentRegion = QRect(50, 50, 50, 80)
        self.x0 = 5
        self.x1 = 25
        self.y0 = 5
        self.y1 = 25
        self.mPixmap = QPixmap()
        self.func = (None, None)

    def initUI(self):
        self.setGeometry(300, 300, 280, 270)
        self.setWindowTitle('Painter training')

        self.pushButton = QPushButton(self)
        self.pushButton.setGeometry(QRect(70, 230, 100, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText('Построить')
        # self.pushButton.clicked.connect(self.drawFlag1(self.qp))

        self.show()

    def paintEvent(self, event):
        if self.mModified:
            pixmap = QPixmap(self.size())
            pixmap.fill(Qt.white)
            painter = QPainter(pixmap)
            painter.drawPixmap(0, 0, self.mPixmap)
            self.drawBackground(painter)
            self.mPixmap = pixmap
            self.mModified = False

        qp = QPainter(self)
        qp.drawPixmap(0, 0, self.mPixmap)
        self.drawFlag(qp)

    def drawBackground(self, qp):
        func, kwargs = self.func
        if func is not None:
            kwargs["qp"] = qp
            func(**kwargs)

    def drawFlag(self, qp):
        print('147')
        qp.setBrush(QColor(255, 0, 0))
        qp.drawRect(30, 30, 120, 30)
        qp.setBrush(QColor(0, 255, 0))
        qp.drawRect(30, 60, 120, 30)
        qp.setBrush(QColor(0, 0, 255))
        qp.drawRect(30, 90, 120, 30)

    def drawFlag1(self, qp):
        print('148')
        qp.setBrush(QColor(255, 0, 0))
        qp.drawRect(30, 30, 120, 30)
        qp.setBrush(QColor(0, 255, 0))
        qp.drawRect(30, 60, 120, 30)
        qp.setBrush(QColor(255, 0, 0))
        qp.drawRect(30, 90, 120, 30)
        self.keyPressEvent1

    def drawFundBlock(self, qp):
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        pen.setStyle(Qt.DashLine)

        qp.setPen(pen)
        for i in range(1, 10):
            qp.drawLine(self.x0, i * self.y0, self.x1, self.y0 * i)

    def drawNumber(self, qp, notePoint):
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        qp.setPen(pen)
        qp.setFont(QFont('Arial', 10))
        qp.drawText(notePoint, "5")

    def nextRegion(self):
        self.x0 += 30
        self.x1 += 30
        self.y0 += 30
        self.y1 += 30

    def keyPressEvent1(self):
        self.update()

    def keyPressEvent(self, event):
        # gey = event.key()
        # self.func = (None, None)
        # if gey == Qt.Key_M:
        #     print("Key 'm' pressed!")
        # elif gey == Qt.Key_Right:
        #     print("Right key pressed!, call drawFundBlock()")
        #     self.func = (self.drawFundBlock, {})
        #     self.mModified = True
        #     self.update()
        #     self.nextRegion()
        # elif gey == Qt.Key_5:
        #     print("#5 pressed, call drawNumber()")
        #     self.func = (self.drawNumber, {"notePoint": QPoint(100, 100)})
        #     self.mModified = True
        #     self.update()
        self.update()


class Example1(QWidget):
    paintTrigger = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.initUI()
        self.ydist = 15
        self.eveType = "drawBlock"
        self.currentRegion = QRect(50, 50, 50, 80)
        # self.paintTrigger[self.eveType].connect(lambda:self.paintEvent())

        self.x0 = 5
        self.x1 = 25
        self.y0 = 5
        self.y1 = 25

    def initUI(self):
        self.setGeometry(300, 300, 280, 270)
        self.setWindowTitle('Painter training')
        self.show()

    # How to pass info here, which type of drawing should be done (block or number)?
    def paintEvent(self, event):
        qp = QPainter(self)
        qp.begin(self)
        self.drawFundBlock(qp)
        qp.end()

    def drawFundBlock(self, qp):
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        pen.setStyle(Qt.DashLine)

        qp.setPen(pen)
        for i in range(1, 10):
            # qp.drawLine(0,i*self.ydist,40,i*self.ydist)
            qp.drawLine(self.x0, i * self.y0, self.x1, self.y0 * i)

        # notePoint=QPoint(200,200)
        # qp.drawText(notePoint,"5")

    def drawNumber(self, qp, notePoint):
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        # qp.setPen(QColor(200,200,200))
        qp.setPen(pen)
        qp.setFont(QFont('Arial', 10))
        qp.drawText(notePoint, "5")

    def nextRegion(self):
        self.x0 = self.x0 + 30
        self.x1 = self.x1 + 30
        self.y0 = self.y0 + 30
        self.y1 = self.y1 + 30

    def keyPressEvent(self, event):
        # Did the user press a button??
        gey = event.key()
        if gey == Qt.Key_M:
            print("Key 'm' pressed!")
        elif gey == Qt.Key_Right:
            print("Right key pressed!, call drawFundBlock()")
            # self.paintTrigger["drawBlock"].emit()
            # self.paintEvent()
            self.update()
            self.nextRegion()

        elif gey == Qt.Key_5:
            print("#5 pressed, call drawNumber()")
            # self.paintTrigger["drawNo"].emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
