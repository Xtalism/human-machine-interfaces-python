import sys, serial, threading
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import *
from ui_arduino_pot_interface import Ui_MainWindow

class main(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(main, self).__init__(parent)
        uic.loadUi('arduino_pot_interface.ui', self)
        self.setWindowTitle('Serial voltage reading')
        self.connectButton.clicked.connect(lambda: threading.Thread(target = self.connect).start())
        
    def connect(self):
        board = serial.Serial('COM3', baudrate=9600, timeout=1)
        
        while True:
            data = board.readline().decode('ascii').rstrip()
            self.potValue.display(data)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = main()
    window.show()
    sys.exit(app.exec())