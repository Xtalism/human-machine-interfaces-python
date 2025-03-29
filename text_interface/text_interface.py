import sys, re
from PyQt6 import uic
from PyQt6.QtWidgets import *
from ui_text import Ui_MainWindow

class main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(main, self).__init__()
        uic.loadUi('text.ui', self)
        self.openFile.clicked.connect(self.open)
            
    def open(self):
        filename = QFileDialog.getOpenFileName(self, caption='File Selection',
                                               filter='File Text(*.txt)')[0]
        self.filePath.clear()
        self.filePath.append(filename)
        pattern = r'(X-DSPAM-Confidence:\s*\d+\.\d+)'
        
        with open(filename, 'r') as file:
            textLines = file.readlines()
            for line in textLines:
                match = re.search(pattern, line)
                if match:
                    data = match.group(1)
                    self.text.appendPlainText(data)
                                    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = main()
    window.show()
    sys.exit(app.exec())