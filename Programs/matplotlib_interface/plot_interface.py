import sys, matplotlib.pyplot as plt
from PyQt6 import uic
from PyQt6.QtWidgets import *
from ui_plot_interface import Ui_MainWindow

class main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('plot_interface.ui', self)
        self.pushButton.clicked.connect(self.open_file)
        self.data = []

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, caption='Select File', 
                                                  filter='Text files (*.txt)')
        if filename:
            self.filePath.clear()
            self.filePath.append(filename)
            self.data.clear()
        
            with open(filename, 'r') as file:
                for line in file:
                        number = int(line.strip())
                        self.data.append(number)
                        self.numberInformation.appendPlainText(str(number))
                self.plot_data()

    def plot_data(self):
        self.save_plot('Scatter Plot', lambda: plt.scatter(range(len(self.data)), self.data))
        self.save_plot('Histogram', lambda: plt.hist(self.data, bins=20, edgecolor='k'))
        plt.show()

    def save_plot(self, title, plot_function):
        plt.figure()
        plot_function()
        plt.title(title)
        
        if 'Scatter' in title:
            plt.xlabel('Index')
            plt.ylabel('Value')
        else:
            plt.xlabel('Value')
            plt.ylabel('Frequency')
        
        fileplot, _ = QFileDialog.getSaveFileName(self, f"Save {title}", "", "JPEG Files (*.jpg)")
        if fileplot:
            plt.savefig(fileplot)
            
        plt.close()
        QMessageBox.information(self, "Information", "Files saved successfully")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = main()
    window.show()
    sys.exit(app.exec())