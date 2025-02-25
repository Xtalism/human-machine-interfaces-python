import sys
from PyQt6 import uic
from PyQt6.QtWidgets import *
from ui_lcd_add_sub import Ui_MainWindow

class main(QMainWindow, Ui_MainWindow):
    def __init__(self): 
        super(main, self).__init__()
        uic.loadUi('lcd_add_sub.ui', self)
        self.boxOperation.currentTextChanged.connect(self.operation)
        
    def operation(self, operate):
        operation_one, operation_two = 0, 0
        operation_one = int(self.inputOne.toPlainText())
        operation_two = int(self.inputTwo.toPlainText())
        
        if operate == 'Add': self.displayNumber.display(operation_one + operation_two)
        if operate == 'Substract': self.displayNumber.display(operation_one - operation_two)
                                    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = main()
    window.show()
    sys.exit(app.exec())