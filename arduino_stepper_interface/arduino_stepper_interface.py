import sys
from datetime import datetime
from PyQt6 import uic, QtCore
from PyQt6.QtWidgets import *
from pymata4 import pymata4
from ui_arduino_stepper_interface import Ui_MainWindow

PHOTORESISTOR_PIN = 0
STEPPER_PINS = [8, 9, 10, 11]
STEPS_PER_REVOLUTION = 2048

board = pymata4.Pymata4()
board.set_pin_mode_analog_input(PHOTORESISTOR_PIN)
board.set_pin_mode_stepper(STEPS_PER_REVOLUTION, STEPPER_PINS)

class StepperMotor(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(StepperMotor, self).__init__()
        uic.loadUi('arduino_stepper_interface.ui', self)
        
        self.movementIteration = 0
        self.table.setRowCount(0)
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["Movement Start #", "Time"])

        self.LIGHT_THRESHOLD = 300
        self.STEPPER_SPEED_RPM = 10
        self.STEPS_PER_INTERVAL = 50

        self.activeMotor = False

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.reading)
        self.timer.start(200)

    def reading(self):
        light_value, _ = board.analog_read(PHOTORESISTOR_PIN)

        if light_value < self.LIGHT_THRESHOLD:
            self.labelsensor.setText(f"No Light (Val: {light_value}) - Motor ON")
            if not self.activeMotor:
                self.activeMotor = True
                self.updateStatus()
            board.stepper_write(self.STEPPER_SPEED_RPM, self.STEPS_PER_INTERVAL)
        else:
            self.labelsensor.setText(f"Light Detected (Val: {light_value}) - Motor OFF")
            if self.activeMotor:
                self.activeMotor = False

    def updateStatus(self):
        self.movementIteration += 1
        currentTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        row = self.table.rowCount()
        self.table.insertRow(row)
        self.table.setItem(row, 0, QTableWidgetItem(str(self.movementIteration)))
        self.table.setItem(row, 1, QTableWidgetItem(currentTime))

    def closeEvent(self, event):
        board.shutdown()
        event.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = StepperMotor()
    ventana.show()
    sys.exit(app.exec())