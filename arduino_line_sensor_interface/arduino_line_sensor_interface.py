import sys
from datetime import datetime
from PyQt6 import uic, QtCore
from PyQt6.QtWidgets import *
from pymata4 import pymata4

board = pymata4.Pymata4()
sensor_pin = 8

class LinearSensor(QMainWindow):
    sensor_data_received = QtCore.pyqtSignal(list)

    def __init__(self):
        super().__init__()
        uic.loadUi('arduino_line_sensor_interface.ui', self)
        
        self.detection_times = []
        self.sensor_data_received.connect(self.update_gui)
        board.set_pin_mode_digital_input(sensor_pin, callback=self.sensor_pin_callback)
        self.pushButton.clicked.connect(self.prepare_to_close)

    def sensor_pin_callback(self, data):
        pin_value = data[2]
        if pin_value == 0:
            event_time = datetime.now().strftime("%H:%M:%S")
            self.detection_times.append(event_time)
            self.sensor_data_received.emit(list(self.detection_times))

    @QtCore.pyqtSlot(list)
    def update_gui(self, data_list):
        self.listWidget.clear()
        self.listWidget.addItems(data_list)

    def prepare_to_close(self):
        with open('timestamps.txt', 'w') as file:
            for time_event in self.detection_times:
                file.write(f"{time_event}\n")
        print("Data saved to Time.txt")
        self.close()

    def closeEvent(self, event):
        event.accept()
        board.shutdown()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = LinearSensor()
    main_window.show()
    sys.exit(app.exec())