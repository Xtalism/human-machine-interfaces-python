import sys, time
from datetime import datetime
from PyQt6 import QtWidgets, QtCore, uic
from PyQt6.QtWidgets import *
from pymata4 import pymata4
from ui_arduino_led_sequence_interface import Ui_MainWindow

board = pymata4.Pymata4()

ledPins = list(range(2, 10))

for pin in ledPins:
    board.set_pin_mode_digital_output(pin)

class worker(QtCore.QObject):
    stared = QtCore.pyqtSignal()
    finish = QtCore.pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.running = False

    @QtCore.pyqtSlot()
    def led_sequence(self):
        self.stared.emit()
        while self.running:
            for pin in ledPins:
                board.digital_write(pin, 1) 
                time.sleep(0.2)  
                board.digital_write(pin, 0) 
        self.finish.emit()

class reading(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None): 
        super(reading, self).__init__(parent)
        uic.loadUi('arduino_led_sequence_interface.ui', self)
        self._worker = worker()
        self._thread = QtCore.QThread(self)
        self._worker.moveToThread(self._thread)
        self._thread.start()
        self._worker.running = True
        QtCore.QTimer.singleShot(0, self._worker.led_sequence)

    def closeEvent(self, event):
        event.accept()
        self._worker.running = False
        self._thread.quit()
        self._thread.wait()
        board.shutdown()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = reading()
    window.show()
    sys.exit(app.exec())