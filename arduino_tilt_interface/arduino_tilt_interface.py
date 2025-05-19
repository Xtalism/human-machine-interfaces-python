import sys
from datetime import datetime
from PyQt6 import uic, QtCore
from PyQt6.QtWidgets import *
from pymata4 import pymata4
from ui_arduino_tilt_interface import Ui_MainWindow

board = pymata4.Pymata4()
SENSOR_PIN = 2  
SERVO_PIN = 6

board.set_pin_mode_digital_input_pullup(SENSOR_PIN)  
board.set_pin_mode_servo(SERVO_PIN)  

class TiltSensor(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(TiltSensor, self).__init__()
        uic.loadUi('arduino_tilt_interface.ui', self)  
        self.movementIteration = 0  
        self.table.setRowCount(0)  
        self.table.setColumnCount(2)  
        self.table.setHorizontalHeaderLabels(["Movement", "Hour"])

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.reading)
        self.timer.start(100)  

    def reading(self):
        sensorState = board.digital_read(SENSOR_PIN)[0]  

        if sensorState== 0:
            self.labelsensor.setText("No movement")
            board.servo_write(SERVO_PIN, 0)  
        elif sensorState == 1:
            self.labelsensor.setText("Movement")
            board.servo_write(SERVO_PIN, 180)  
            self.updateStatus()  

    def updateStatus(self):
        self.movementIteration += 1 
        currentTime = datetime.now().strftime("%H:%M:%S")

        row = self.table.rowCount()
        self.table.insertRow(row)
        self.table.setItem(row, 0, QTableWidgetItem(str(self.movementIteration)))
        self.table.setItem(row, 1, QTableWidgetItem(currentTime))

    def closeEvent(self):
        board.servo_write(SERVO_PIN, 0)  
        board.shutdown()
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = TiltSensor()
    ventana.show()
    sys.exit(app.exec())