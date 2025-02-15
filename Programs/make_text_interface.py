import sys, re
from PyQt6 import uic
from PyQt6.QtWidgets import *
from ui_write_text import Ui_MainWindow

class main(QMainWindow, Ui_MainWindow):
    def __init__(self): 
        super(main, self).__init__()
        uic.loadUi('write_text.ui', self)
        self.buttonWrite.clicked.connect(self.writing)
        
    def writing(self):
        filename = QFileDialog.getSaveFileName(self, caption='Save file',
                                               filter='txt File(*.txt)')[0]
        file = open(filename, 'w')
        text = self.plainTextEdit.toPlainText()
        file.write(text)
        file.close()
                                    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = main()
    window.show()
    sys.exit(app.exec())