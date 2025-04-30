import sys, random
from PyQt6 import uic
from PyQt6.QtCore import QTimer 
from PyQt6.QtWidgets import *
from pymata4 import pymata4

board = pymata4.Pymata4()

board.set_pin_mode_pwm_output(3)
board.set_pin_mode_pwm_output(5)
board.set_pin_mode_pwm_output(6)

class Colors(QMainWindow):
    def __init__(self, parent=None):
        super(Colors, self).__init__(parent)
        uic.loadUi('arduino_rgb_interface.ui', self)
        self.redColor: QLineEdit = self.findChild(QLineEdit, "redColor")
        self.greenColor: QLineEdit = self.findChild(QLineEdit, "greenColor")
        self.blueColor: QLineEdit = self.findChild(QLineEdit, "blueColor")
        self.frameColor: QFrame = self.findChild(QFrame, "frameColor")

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_random_color)
        self.timer.start(500)

    def update_random_color(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

        self.redColor.setText(str(r))
        self.greenColor.setText(str(g))
        self.blueColor.setText(str(b))

        frame_rgb = f'QFrame {{ background-color: rgb({r},{g},{b}); }}'
        self.frameColor.setStyleSheet(frame_rgb)

        board.pwm_write(3, r)
        board.pwm_write(5, g)
        board.pwm_write(6, b)

    def closeEvent(self, event):
        self.timer.stop()
        board.shutdown()
        event.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Colors()
    window.show()
    sys.exit(app.exec())