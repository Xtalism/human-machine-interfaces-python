import sys
from PyQt6 import uic
from PyQt6.QtWidgets import *
from ui_adder import Ui_MainWindow

class adder(QMainWindow, Ui_MainWindow):
    def __init__(self): 
        super(adder, self).__init__()
        uic.loadUi('adder.ui', self)
        self.setWindowTitle('Adder')
        self.additionButton.clicked.connect(self.addition)
        
    def addition(self):
        try:
            operation_one, operation_two = 0, 0
            operation_one = float(self.dataA.text())
            operation_two = float(self.dataB.text())
            self.textEdit.setText(str(operation_one + operation_two))
        
        except ValueError:
            QMessageBox.warning(self, 'Error', 'Input float numbers!')
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = adder()
    window.show()
    sys.exit(app.exec())