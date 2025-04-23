import sys, time
from pymata4 import pymata4
from PyQt6 import QtCore, uic
from PyQt6.QtWidgets import QMainWindow, QApplication
from ui_arduino_sequence_interface import Ui_MainWindow

board = pymata4.Pymata4()

for pin in range(2, 9):
    board.set_pin_mode_digital_output(pin)

class worker(QtCore.QObject):
    stared = QtCore.pyqtSignal()
    finish = QtCore.pyqtSignal()
    led_sequence = QtCore.pyqtSignal(list)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.running = False
        
    @QtCore.pyqtSlot()
    def run_sequence(self):
        for pin in range(8, 1, -1):
            board.digital_write(pin, 1)
            time.sleep(0.2)
            board.digital_write(pin, 0)
        self.finish.emit()

class writing(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None): 
        super(writing, self).__init__(parent)
        uic.loadUi('arduino_sequence_interface.ui', self)
        self._worker = worker()
        self._thread = QtCore.QThread(self)
        self._thread.start()
        self._worker.moveToThread(self._thread)
        self._worker.running = True
        
        self.startButton.clicked.connect(self._worker.run_sequence)
        self._thread.start()
                        
    def closeEvent(self, event):
        event.accept()
        board.shutdown()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = writing()
    window.show()
    sys.exit(app.exec())