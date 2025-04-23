import sys, time
from pymata4 import pymata4
from PyQt6 import QtCore, uic
from PyQt6.QtWidgets import QMainWindow, QApplication
from ui_arduino_voltmeter_interface import Ui_MainWindow

board = pymata4.Pymata4()
board.set_pin_mode_analog_input(0)

for pin in range(2, 7):
    board.set_pin_mode_digital_output(pin)

class worker(QtCore.QObject):
    stared = QtCore.pyqtSignal()
    finish = QtCore.pyqtSignal()
    data_volt = QtCore.pyqtSignal(list)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.running = False

    @QtCore.pyqtSlot()
    def sensor(self):
        self.stared.emit()
        while self.running:
            self.data_volt.emit(board.analog_read(0))
            time.sleep(0.1)
        self.finish.emit()
    
class reading(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None): 
        super(reading, self).__init__(parent)
        uic.loadUi('arduino_voltmeter_interface.ui', self)
        self._worker = worker()
        self._worker.data_volt.connect(self.update_gui)
        self._thread = QtCore.QThread(self)
        self._thread.start()
        self._worker.moveToThread(self._thread)
        self._worker.running = True
        QtCore.QTimer.singleShot(0, self._worker.sensor)

    @QtCore.pyqtSlot(list)
    def update_gui(self, data_volt):
        voltageValue = data_volt[0] * 5 / 1023
        self.potValue.display(voltageValue)
        
        for pin in range(2, 7):
            threshold = pin - 1
            state = 1 if voltageValue >= threshold else 0
            board.digital_write(pin, state) 
                        
    def closeEvent(self, event):
        event.accept()
        board.shutdown()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = reading()
    window.show()
    sys.exit(app.exec())