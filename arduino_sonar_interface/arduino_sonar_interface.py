import sys, time
from PyQt6 import QtCore, uic
from PyQt6.QtWidgets import *
from pymata4 import pymata4

board = pymata4.Pymata4()
ECHO = 2
TRIGGER = 3
board.set_pin_mode_sonar(TRIGGER, ECHO)

for pin in range(4, 8):
    board.set_pin_mode_digital_output(pin)

def ledControl(ledPinOn):
    board.digital_write(ledPinOn, 1)
    for i in range(4, 8):
        if i != ledPinOn:
            board.digital_write(i, 0)
    board.digital_write(7, ledPinOn == 4) # buzzer
            
def frameColor(r, g, b):
    return f'QFrame {{ background-color: rgb({r},{g},{b}); }}'

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
            self.data_ultra.emit(board.sonar_read(TRIGGER))
            time.sleep(0.1)
        self.finish.emit()
    
class reading(QMainWindow):
    def __init__(self, parent=None): 
        super(reading, self).__init__(parent)
        uic.loadUi('arduino_sonar_interface.ui', self)
        self._worker = worker()
        self._worker.data_ultra.connect(self.updateGui)
        self._thread = QtCore.QThread(self)
        self._thread.start()
        self._worker.moveToThread(self._thread)
        self._worker.running = True
        QtCore.QTimer.singleShot(0, self._worker.sensor)
        self.label: QLabel = self.findChild(QLabel, "distance")
        self.frameColor: QFrame = self.findChild(QFrame, "frameColor")
        
    @QtCore.pyqtSlot(list)
    def updateGui(self, data_ultra):
        self.sonarReading.display(data_ultra[0])
        
        if data_ultra[0] < 10:
            style = frameColor(255, 0, 0)
            ledControl(4)
            self.label.setText("Near")
        elif data_ultra[0] > 10 and data_ultra[0] <= 20:
            style = frameColor(255, 255, 0)
            ledControl(5)
            self.label.setText("Medium")
        else:
            style = frameColor(0, 0, 255)
            ledControl(6)
            self.label.setText("Far")
        self.frameColor.setStyleSheet(style)
            
    def closeEvent(self, event):
        event.accept()
        board.shutdown()
                        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = reading()
    window.show()
    sys.exit(app.exec())