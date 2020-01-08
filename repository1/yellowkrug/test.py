import sys
from PyQt5 import QtGui, QtCore, QtWidgets

class Example(QtWidgets.QWidget):

    draw = False

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()
        self.test = self

    def initUI(self):

        self.setGeometry(400, 400, 400, 400)

        qbtn = QtWidgets.QPushButton('Paint', self)
        # self.pushBuild = QtWidgets.QPushButton()

        qbtn.clicked.connect(self.buttn)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Paint')
        self.show()

    def paintEvent(self, e):

        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawRectangles(qp)
        qp.end()

    def drawRectangles(self, qp):

        if self.draw:
            qp.setBrush(QtGui.QColor(000, 000, 255))
            qp.drawRect(0, 0, 90, 60)

    @QtCore.pyqtSlot()
    def buttn(self):
        self.draw = True


def main():

    app = QtWidgets.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Dialog = QtWidgets.QWidget()
#     ui = Ui_Dialog()
#     ui.setupUi(Dialog)
#     Dialog.show()
#     sys.exit(app.exec_())