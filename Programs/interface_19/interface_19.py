import sys, re, numpy as np
from PyQt6.QtWidgets import *
from PyQt6 import uic
from ui_interface19 import Ui_MainWindow

class main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(main, self).__init__()
        uic.loadUi('interface_19.ui', self)
        self.openFile.clicked.connect(self.open)
        self.data = []

    def open(self):
        self.filePath.clear()
        filename, _ = QFileDialog.getOpenFileName(self, caption='Select Text File', 
                                                  filter='Text File (*.txt)')
        self.filePath.append(filename)
        if filename:
            self.text.clear()
            pattern = r'X-DSPAM-Confidence:\s*(\d+\.\d+)'

            with open(filename, 'r') as file:
                lines = file.readlines()
                
                for line in lines:
                    match = re.search(pattern, line)
                    if match:
                        data_s = float(match.group(1))
                        self.data.append(data_s)
                        
            self.calculate(self.data)

    def calculate(self, value):
        quantity = len(value)
        addition = sum(value)
        
        if quantity > 0:
            average = addition / quantity
            variance = np.var(value)
        else:
            average = 0
            variance = 0

        self.text.appendPlainText(f'Data quantity: {quantity}')
        self.text.appendPlainText(f'Data sumatory: {addition}')
        self.text.appendPlainText(f'Data average: {average}')
        self.text.appendPlainText(f'Data variance: {variance}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = main()
    dialog.show()
    sys.exit(app.exec())