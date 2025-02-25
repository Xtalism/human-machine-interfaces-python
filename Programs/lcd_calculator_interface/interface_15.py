import sys
from PyQt6 import uic
from PyQt6.QtWidgets import *
from ui_interface_15 import Ui_MainWindow

class main(QMainWindow, Ui_MainWindow):
    def __init__(self): 
        super(main, self).__init__()
        uic.loadUi('interface_15.ui', self)
        self.buttonAdd.clicked.connect(self.add)
        self.buttonSubstract.clicked.connect(self.substract)
        self.buttonMultiply.clicked.connect(self.multiply)
        self.buttonDivide.clicked.connect(self.divide)
                
    def add(self):
        try:
            operation_one, operation_two = 0, 0
            operation_one = float(self.dataA.text())
            operation_two = float(self.dataB.text())
            self.displayNumber.display(operation_one + operation_two)
        
        except ValueError:
            QMessageBox.warning(self, 'Error', 'Input float numbers!')

    def substract(self):
        try:
            operation_one, operation_two = 0, 0
            operation_one = float(self.dataA.text())
            operation_two = float(self.dataB.text())
            self.displayNumber.display(operation_one - operation_two)
        
        except ValueError:
            QMessageBox.warning(self, 'Error', 'Input float numbers!')
            
    def multiply(self):
        try:
            operation_one, operation_two = 0, 0
            operation_one = float(self.dataA.text())
            operation_two = float(self.dataB.text())
            self.displayNumber.display(operation_one * operation_two)
        
        except ValueError:
            QMessageBox.warning(self, 'Error', 'Input float numbers!')
            
    def divide(self):
        try:
            operation_one, operation_two = 0, 0
            operation_one = float(self.dataA.text())
            operation_two = float(self.dataB.text())
            self.displayNumber.display(operation_one / operation_two)
        
        except ValueError:
            QMessageBox.warning(self, 'Error', 'Input float numbers!')
                
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = main()
    window.show()
    sys.exit(app.exec())