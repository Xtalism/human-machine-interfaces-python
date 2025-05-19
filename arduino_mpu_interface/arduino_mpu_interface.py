import sys, time
from PyQt6 import QtCore, uic
from PyQt6.QtWidgets import *
from pymata4 import pymata4

MPU_ADDRESS = 0x68
PWR_MGMT_1 = 0x6B
ACCEL_XOUT_H = 0x3B

class Worker(QtCore.QObject):
    data_mpu = QtCore.pyqtSignal(list)
    finished = QtCore.pyqtSignal()
    
    def __init__(self, board_instance):
        super().__init__()
        self.board = board_instance
        self.running = True
        
    def read_mpu6050(self):
        self.board.i2c_write(MPU_ADDRESS, [PWR_MGMT_1, 0])
        time.sleep(0.1)
        
        while self.running:
            data = self.board.i2c_read(MPU_ADDRESS, ACCEL_XOUT_H, 14)
            
            if data:
                processed = [
                    self.twos_complement(data[0], data[1]) / 16384.0,  # Accel X
                    self.twos_complement(data[2], data[3]) / 16384.0,  # Accel Y
                    self.twos_complement(data[4], data[5]) / 16384.0,  # Accel Z
                    self.twos_complement(data[8], data[9]) / 131.0,    # Gyro X
                    self.twos_complement(data[10], data[11]) / 131.0,  # Gyro Y
                    self.twos_complement(data[12], data[13]) / 131.0,  # Gyro Z
                    self.twos_complement(data[6], data[7]) / 340 + 36.53  # Temp
                ]
                self.data_mpu.emit(processed)
        time.sleep(0.1)
            
        self.finished.emit()
    
    def twos_complement(self, high, low):
        val = (high << 8) | low
        return val - 65536 if val > 32767 else val

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('arduino_mpu_interface.ui', self)
        self.board = pymata4.Pymata4()
        self.worker = Worker(self.board)
        self.thread = QtCore.QThread()
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.read_mpu6050)
        self.worker.data_mpu.connect(self.update_display)
        self.listWidget = self.findChild(QListWidget, "listWidget") 
        self.thread.start()
        
    def update_display(self, data):
        if hasattr(self, 'listWidget') and self.listWidget is not None and data:
            self.listWidget.clear()
            labels = ["Accel X", "Accel Y", "Accel Z", 
                     "Gyro X", "Gyro Y", "Gyro Z", 
                     "Temperature"]
            if len(data) == len(labels):
                for label, value in zip(labels, data):
                    if value is not None:
                        self.listWidget.addItem(f"{label}: {value:.2f}")
                    else:
                        self.listWidget.addItem(f"{label}: N/A")
            else:
                self.listWidget.addItem("Error: Malformed data received")

    def closeEvent(self, event):
        self.worker.running = False
        self.thread.quit()
        self.thread.wait()
        self.board.shutdown()
        event.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())