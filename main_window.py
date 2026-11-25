from PyQt6.QtWidgets import QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtGui import QPixmap, QPainter, QColor
from PyQt6.QtCore import Qt
import random


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.drawArea = QLabel()
        self.drawArea.setMinimumSize(400, 300)
        self.drawArea.resize(600, 400)
        self.button = QPushButton("Создать круг")

        layout = QVBoxLayout()
        layout.addWidget(self.drawArea)
        layout.addWidget(self.button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.circles = []
        self.button.clicked.connect(self.create_circle)

    def create_circle(self):
        width = self.drawArea.width()
        height = self.drawArea.height()
        diameter = random.randint(20, 100)
        x = random.randint(0, max(0, width - diameter))
        y = random.randint(0, max(0, height - diameter))
        color = QColor(
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )
        self.circles.append((x, y, diameter, color))
        self.draw_circles()

    def draw_circles(self):
        pixmap = QPixmap(self.drawArea.size())
        pixmap.fill(Qt.GlobalColor.white)

        painter = QPainter(pixmap)

        for x, y, diameter, color in self.circles:
            painter.setBrush(color)
            painter.drawEllipse(x, y, diameter, diameter)

        painter.end()
        self.drawArea.setPixmap(pixmap)
