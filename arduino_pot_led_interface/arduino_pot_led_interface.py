import sys
from PyQt6 import uic
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import *
from pymata4 import pymata4

board = pymata4.Pymata4()

RED = 3 
GREEN = 5
BLUE = 6

POT_RED = 0
POT_GREEN = 1
POT_BLUE = 2

led_pins_for_setup = [RED, GREEN, BLUE]
for pin in led_pins_for_setup:
    board.set_pin_mode_pwm_output(pin)

pot_pins_for_setup = [POT_RED, POT_GREEN, POT_BLUE]
for pin in pot_pins_for_setup:
    board.set_pin_mode_analog_input(pin)

class RGB(QMainWindow):
    def __init__(self, parent=None):
        super(RGB, self).__init__(parent)
        uic.loadUi('arduino_pot_led_interface.ui', self)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.led_colors)
        self.timer.start(20)  

    def reading(self, pin_pot, pin_led):
        analog_value, _ = board.analog_read(pin_pot)
        pwm_value = int(analog_value / 1023 * 255)
        board.pwm_write(pin_led, pwm_value)
        return pwm_value

    def led_colors(self):
        r_pwm = self.reading(POT_RED, RED)
        g_pwm = self.reading(POT_GREEN, GREEN)
        b_pwm = self.reading(POT_BLUE, BLUE)
        
        self.redText.setText(str(r_pwm))
        self.greenText.setText(str(g_pwm))
        self.blueText.setText(str(b_pwm))
        
        color_rgb = f'QFrame{{background-color:rgb({r_pwm},{g_pwm},{b_pwm});}}'
        self.frame.setStyleSheet(color_rgb)

    def closeEvent(self, event):
        board.shutdown()
        event.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RGB()
    window.show()
    sys.exit(app.exec())