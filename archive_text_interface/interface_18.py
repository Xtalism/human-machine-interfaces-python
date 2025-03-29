import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
from text_ui import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self): 
        super().__init__()
        uic.loadUi('text.ui', self)
        self.openFile.clicked.connect(self.open)
            
    def open(self):
        filename = QFileDialog.getOpenFileName(self, caption='File Selection', 
                                               filter='Text Files (*.txt)')[0]
        self.filePath.clear()
        self.filePath.setText(filename) 
        
        with open(filename, 'r') as file:
            textLines = file.readlines()
            self.text.clear() 
            
            lineNumber = len(textLines)
            totalWords = 0
            totalCharacters = 0
            
            for line in textLines:
                totalWords += len(line.split()) 
                totalCharacters += len(line)
            
            self.text.appendPlainText(f'Number of lines: {lineNumber}')
            self.text.appendPlainText(f'Number of words: {totalWords}')
            self.text.appendPlainText(f'Number of characters: {totalCharacters}')
                                    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())