import sys
from PyQt6 import uic
from PyQt6.QtCore import QTimer 
from PyQt6.QtWidgets import *
from pymata4 import pymata4

X_PIN = 0
Y_PIN = 1
# BUTTON_PIN = 2

ACTIVE_COLOR = (0, 255, 0)
INACTIVE_COLOR = (255, 0, 0)

THRESHOLD_LOW = 300
THRESHOLD_HIGH = 700

board = pymata4.Pymata4()
board.set_pin_mode_analog_input(X_PIN) 
board.set_pin_mode_analog_input(Y_PIN)
# board.set_pin_mode_digital_input_pullup(BUTTON_PIN) 

class Joystick(QMainWindow):
    def __init__(self, parent=None):
        super(Joystick, self).__init__(parent)
        uic.loadUi('arduino_joystick_interface.ui', self)
        self.frameUp: QFrame = self.findChild(QFrame, "up")
        self.frameRight: QFrame = self.findChild(QFrame, "right")
        self.frameDown: QFrame = self.findChild(QFrame, "down")
        self.frameLeft: QFrame = self.findChild(QFrame, "left")
        self.all_frames = [self.frameLeft, self.frameRight, self.frameUp, self.frameDown]
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_gui)
        self.timer.start(100) 
    
    def setFrameColor(self, frame: QFrame, r, g, b):
        style = f'QFrame {{ background-color: rgb({r},{g},{b}); }}'
        frame.setStyleSheet(style)

    def update_gui(self):
        x, _ = board.analog_read(X_PIN)
        y, _ = board.analog_read(Y_PIN)
        # button, _ = board.digital_read(BUTTON_PIN)

        for frame in self.all_frames:
            self.setFrameColor(frame, *INACTIVE_COLOR)
        
        if x < THRESHOLD_LOW:
            self.setFrameColor(self.frameLeft, *ACTIVE_COLOR)
        if x > THRESHOLD_HIGH:
            self.setFrameColor(self.frameRight, *ACTIVE_COLOR)
        
        if y < THRESHOLD_LOW:
             self.setFrameColor(self.frameUp, *ACTIVE_COLOR)
        if y > THRESHOLD_HIGH:
             self.setFrameColor(self.frameDown, *ACTIVE_COLOR)

    def closeEvent(self, event):
        board.shutdown()
        event.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Joystick()
    window.show()
    sys.exit(app.exec())