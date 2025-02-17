import sys
from PyQt6 import uic
from PyQt6.QtWidgets import *
from ui_archive_text import Ui_MainWindow

class main(QMainWindow, Ui_MainWindow):
    def __init__(self): 
        super(main, self).__init__()
        uic.loadUi('archive_text.ui', self)
        
                
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = main()
    window.show()
    sys.exit(app.exec())