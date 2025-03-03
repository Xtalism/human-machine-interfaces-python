import sys, pandas as pd, matplotlib.pyplot as plt
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap
from ui_pib_excel import Ui_MainWindow 

class main(QMainWindow, Ui_MainWindow):
    def __init__(self): 
        super(main, self).__init__()
        uic.loadUi('pib_excel.ui', self)
        self.openFile.clicked.connect(self.open_excel)
                
    def open_excel(self):
        self.textBrowser.clear()
        filename = QFileDialog.getOpenFileName(self, caption='Select Excel File', 
                                               filter='Excel File (*.xls, *.xlsx)')[0]
        self.textBrowser.append(filename)
        self.read_excel(filename)
        
    def read_excel(self, path):
        df = pd.read_excel(path)
        df['PIB anual'] = df['PIB anual'].replace(r'\.', '', regex = True).astype(int)
        df = df.sort_values('PIB anual', ascending = False)
        df = df.head(15)
        
        datas = df.values.tolist()
        self.tableWidget.setRowCount(df.shape[0])
        self.tableWidget.setColumnCount(df.shape[1])
        self.tableWidget.setHorizontalHeaderLabels(df.columns.tolist())
        
        for rindex, data in enumerate(datas):
            for cindex, rdata in enumerate(data):
                self.tableWidget.setItem(rindex, cindex, QtWidgets.QTableWidgetItem(str(rdata)))
                
        fig, ax = plt.subplots(figsize=(20, 6))
        ax.bar(df['Países'], df['PIB anual'])
        fig.tight_layout()
        fig.savefig('graph.png')
        
        display_graph = QPixmap('graph.png')
        self.image.setPixmap(display_graph)
        self.image.setScaledContents(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = main()
    window.show()
    sys.exit(app.exec())