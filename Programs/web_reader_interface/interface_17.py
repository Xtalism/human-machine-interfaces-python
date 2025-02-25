import sys
from PyQt6 import uic
from PyQt6.QtWidgets import *
from ui_web_reader import Ui_MainWindow
from urllib import request
from urllib.error import URLError

class main(QMainWindow, Ui_MainWindow):
    def __init__(self): 
        super(main, self).__init__()
        uic.loadUi('web_reader.ui', self)
        self.readContent.clicked.connect(self.webReading)
        
    def webReading(self):
        try:
            url = self.plainTextEdit.toPlainText()
            file = request.urlopen(url)
            data = file.read().decode('utf-8')
            display = self.text.setPlainText(data)
            file.read(display)

        except URLError:
            return(f'The url {url} does not exist!')
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = main()
    window.show()
    sys.exit(app.exec())