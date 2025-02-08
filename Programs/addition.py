import sys
from PyQt6 import uic
from PyQt6.QtWidgets import *
from adder_ui import Ui_MainWindow

class adder(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(adder, self).__init__()
        uic.loadUi('adder.ui', self)
        self.dataA
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = adder()
    window.show()
    sys.exit(app.exec())    