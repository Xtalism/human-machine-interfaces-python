import sys, serial, time
from PyQt6 import uic
from PyQt6.QtWidgets import *
from ui_arduino_led_interface import Ui_MainWindow

class main(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(main, self).__init__(parent)
        uic.loadUi('arduino_led_interface.ui', self)
        self.setWindowTitle('Led control')
        self.powerOn.clicked.connect(self.turn_on)
        self.powerOff.clicked.connect(self.turn_off)
        
    def turn_on(self):
        board = serial.Serial('COM3', baudrate=9600, timeout=1)
        time.sleep(1)
        board.write(b'1')
        board.close()
        
    def turn_off(self):
        board = serial.Serial('COM3', baudrate=9600, timeout=1)
        time.sleep(1)
        board.write(b'0')
        board.close()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = main()
    window.show()
    sys.exit(app.exec())