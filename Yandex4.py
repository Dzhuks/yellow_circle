import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
from yellow_circle import Ui_MainWindow
from PyQt5.QtGui import QPainter, QPen, QColor


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
        qp.setBrush(QColor(255, 255, 0))
        qp.setPen(QPen(Qt.yellow, 1, Qt.SolidLine))
        qp.drawEllipse(100, 100, 100, 100)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
