from PyQt5.QtCore import QThread, QTimer
from PyQt5.QtWidgets import QLabel, QWidget, QPushButton, QVBoxLayout, QApplication, QHBoxLayout, QMessageBox,  QMainWindow
from PyQt5.QtGui import QPixmap, QImage
from models import Camera


class UI_Window(QWidget):

    def __init__(self, cam_num):
        super().__init__()
        self.cam_num = cam_num
        self.cam_num.open()
        # Create a timer.
        self.timer = QTimer()
        self.timer.timeout.connect(self.nextFrameSlot)
        self.timer.start(1000. / 24)
        layout = QVBoxLayout()
        button_layout = QHBoxLayout()
        btnCamera = QPushButton("Print Brightness")
        btnCamera.clicked.connect(self.print_brightness)
        button_layout.addWidget(btnCamera)
        layout.addLayout(button_layout)
        # Add a label
        self.setLayout(layout)

    def nextFrameSlot(self):
        frame = self.cam_num.read()
        if frame is not None:
            image = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
            self.pixmap = QPixmap.fromImage(image)

    def print_brightness(self):
         self.cam_num.set_brightness(0.5)
         print(self.cam_num.get_brightness())
