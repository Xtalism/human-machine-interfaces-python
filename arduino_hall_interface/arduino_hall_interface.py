import sys
from PyQt6 import uic
from PyQt6.QtCore import QTimer 
from PyQt6.QtWidgets import *
from pymata4 import pymata4

board = pymata4.Pymata4()

GREEN_LED_PIN = 10
RED_LED_PIN = 9
HALL_DIGITAL_PIN = 3
HALL_ANALOG_PIN = 0
UPDATE_INTERVAL = 100
TOLERANCE = 540

board.set_pin_mode_digital_input(HALL_DIGITAL_PIN)
board.set_pin_mode_analog_input(HALL_ANALOG_PIN)

board.set_pin_mode_digital_output(GREEN_LED_PIN)
board.set_pin_mode_digital_output(RED_LED_PIN)

class HallSensor(QMainWindow):
    def __init__(self, parent=None):
        super(HallSensor, self).__init__(parent)
        uic.loadUi('arduino_hall_interface.ui', self)
        self.frameColor: QFrame = self.findChild(QFrame, "frameColor")
        self.labelMagnetPolarity : QLabel = self.findChild(QLabel, "magnetPolarity")

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_status)
        self.timer.start(UPDATE_INTERVAL)

    def update_status(self):
        digitalValue, _ = board.digital_read(HALL_DIGITAL_PIN)
        analogValue, _ = board.analog_read(HALL_ANALOG_PIN)
        
        if digitalValue == 1 and analogValue < TOLERANCE:
            board.digital_write(GREEN_LED_PIN, 1)
            board.digital_write(RED_LED_PIN, 0)
            frame_rgb = f'QFrame {{ background-color: rgb({0},{255},{0}); }}'
            self.labelMagnetPolarity.setText('North Pole') 
        else:
            board.digital_write(GREEN_LED_PIN, 0)
            board.digital_write(RED_LED_PIN, 1)
            frame_rgb = f'QFrame {{ background-color: rgb({255},{0},{0}); }}'
            self.labelMagnetPolarity.setText(f"{analogValue}") 
            self.labelMagnetPolarity.setText('South Pole') 
                                   
        self.frameColor.setStyleSheet(frame_rgb)

    def closeEvent(self, event):
        board.shutdown()
        event.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HallSensor()
    window.show()
    sys.exit(app.exec())