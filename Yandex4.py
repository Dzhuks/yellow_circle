import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
from yellow_circle import Ui_MainWindow
from PyQt5.QtGui import QPainter, QPen, QColor
from random import randrange


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.initUI()

    def initUI(self):
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()
        self.do_paint = False

    def draw_circle(self, qp):
        random_color = QColor(randrange(256), randrange(256), randrange(256))
        qp.setBrush(random_color)
        qp.setPen(QPen(Qt.yellow, 1, Qt.SolidLine))
        radius = randrange(50, 100)
        qp.drawEllipse(100, 100, radius, radius)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
