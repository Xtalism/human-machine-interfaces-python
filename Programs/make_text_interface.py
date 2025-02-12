import sys
from PyQt6 import uic
from PyQt6.QtWidgets import *

class functionName(QMainWindow):
    def __init__(self): 
        super(functionName, self).__init__()
        uic.loadUi('', self)
                
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = functionName()
    window.show()
    sys.exit(app.exec())