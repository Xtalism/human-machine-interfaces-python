import sys, collections, math
from PyQt6 import uic
from PyQt6.QtCore import QTimer 
from PyQt6.QtWidgets import *
from pymata4 import pymata4
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure

board = pymata4.Pymata4()
board.set_pin_mode_dht(2, 11, 0.5)

UPDATE_INTERVAL = 1000  # milliseconds
DATA_POINTS = 20

class main(QMainWindow):
    def __init__(self, parent=None):
        super(main, self).__init__(parent)
        uic.loadUi('arduino_dht11_interface.ui', self)
        self.widget: QWidget = self.findChild(QWidget, "dhtGraph")
        self.label: QLineEdit = self.findChild(QLineEdit, "heatIndex")

        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvasQTAgg(self.fig)
        
        layout = QVBoxLayout(self.widget)
        self.widget.setLayout(layout)
        self.widget.layout().addWidget(self.canvas)

        self.time_data = collections.deque(maxlen=DATA_POINTS)
        self.humidity_data = collections.deque(maxlen=DATA_POINTS)
        self.temperature_data = collections.deque(maxlen=DATA_POINTS)
        self.time_counter = 0

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_status)
        self.timer.start(UPDATE_INTERVAL)
        
    def computeHeatIndex(self, temperature_c, humidity):
        temperature_f = temperature_c * 1.8 + 32

        hi_f = 0.5 * (temperature_f + 61.0 + ((temperature_f - 68.0) * 1.2) + (humidity * 0.094))

        if hi_f > 79:
            hi_f = (-42.379 +
                    2.04901523 * temperature_f +
                    10.14333127 * humidity +
                    -0.22475541 * temperature_f * humidity +
                    -0.00683783 * math.pow(temperature_f, 2) +
                    -0.05481717 * math.pow(humidity, 2) +
                    0.00122874 * math.pow(temperature_f, 2) * humidity +
                    0.00085282 * temperature_f * math.pow(humidity, 2) +
                    -0.00000199 * math.pow(temperature_f, 2) * math.pow(humidity, 2))

            if humidity < 13 and 80.0 <= temperature_f <= 112.0:
                adjustment = ((13.0 - humidity) * 0.25) * math.sqrt((17.0 - abs(temperature_f - 95.0)) * 0.05882)
                hi_f -= adjustment
            elif humidity > 85.0 and 80.0 <= temperature_f <= 87.0:
                adjustment = ((humidity - 85.0) * 0.1) * ((87.0 - temperature_f) * 0.2)
                hi_f += adjustment

        hi_c = (hi_f - 32) * 0.55555
        return hi_c
        
    def update_status(self):
        dhtValues = board.dht_read(2)
        humidity = dhtValues[0]
        temperature = dhtValues[1]
        heat_index = self.computeHeatIndex(temperature, humidity)

        self.time_data.append(self.time_counter)
        self.humidity_data.append(humidity)
        self.temperature_data.append(temperature)
        self.time_counter += 1

        self.ax.cla()
        self.ax.plot(self.time_data, self.humidity_data, label='Humidity', color='blue')
        self.ax.plot(self.time_data, self.temperature_data, label='Temperature', color='red')
        self.ax.set_xlabel('Time (s)')
        self.ax.set_ylabel('Values')
        self.ax.set_title('DHT11 Sensor Data')
        self.ax.legend()
        self.canvas.draw()
        
        self.heatIndex.setText(f"Heat Index: {heat_index:.2f} °C")
        
    def closeEvent(self, event):
        board.shutdown()
        event.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = main()
    window.show()
    sys.exit(app.exec())