from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPixmap, QPainter, QColor
from PyQt6.QtCore import Qt
from PyQt6 import uic
import sys
import random


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.circles = []
        self.button.clicked.connect(self.create_circle)

    def create_circle(self):
        width = self.drawArea.width()
        height = self.drawArea.height()
        diameter = random.randint(20, 100)
        x = random.randint(0, max(0, width - diameter))
        y = random.randint(0, max(0, height - diameter))
        self.circles.append((x, y, diameter))
        self.draw_circles()

    def draw_circles(self):
        pixmap = QPixmap(self.drawArea.size())
        pixmap.fill(Qt.GlobalColor.white)

        painter = QPainter(pixmap)
        painter.setBrush(QColor("yellow"))

        for x, y, diameter in self.circles:
            painter.drawEllipse(x, y, diameter, diameter)

        painter.end()
        self.drawArea.setPixmap(pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
