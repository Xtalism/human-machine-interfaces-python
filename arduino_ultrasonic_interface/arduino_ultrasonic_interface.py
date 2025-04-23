import sys, time
from datetime import datetime
from PyQt6 import QtWidgets, QtCore, uic
from PyQt6.QtWidgets import *
from pymata4 import pymata4
from ui_arduino_ultrasonic_interface import Ui_MainWindow

board = pymata4.Pymata4()
echo = 2
trigger = 3
board.set_pin_mode_sonar(trigger, echo)

class worker(QtCore.QObject):
    stared = QtCore.pyqtSignal()
    finish = QtCore.pyqtSignal()
    data_ultra = QtCore.pyqtSignal(list)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.running = False
    
    @QtCore.pyqtSlot()
    def sensor(self):
        self.stared.emit()
        while self.running:
            self.data_ultra.emit(board.sonar_read(trigger))
        time.sleep(0.1)
        self.finish.emit()
    
class reading(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None): 
        super(reading, self).__init__(parent)
        uic.loadUi('arduino_ultrasonic_interface.ui', self)
        self._worker = worker()
        self._worker.data_ultra.connect(self.update_gui)
        self._thread = QtCore.QThread(self)
        self._thread.start()
        self._worker.moveToThread(self._thread)
        self._worker.running = True
        QtCore.QTimer.singleShot(0, self._worker.sensor)
        
    @QtCore.pyqtSlot(list)
    def update_gui(self, data_ultra):
        self.milimeterReading.display(data_ultra[0])        
        self.inchesReading.display(data_ultra[0] / 2.54)        
        # now = datetime.now()
        # self.hourLabel.setText(now.strftime('%H:%M%:%S'))

    def closeEvent(self, event):
        event.accept()
        board.shutdown()
                        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = reading()
    window.show()
    sys.exit(app.exec())