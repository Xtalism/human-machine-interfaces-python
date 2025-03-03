import sys, pathlib, pandas as pd
from io import BytesIO
from zipfile import ZipFile
from PyQt6.QtWidgets import *
from PyQt6 import QtWidgets, uic
from urllib.request import urlopen
from ui_extract_zip import Ui_MainWindow

class main(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs): 
        super(main, self).__init__(*args, **kwargs)
        uic.loadUi('extract_zip.ui', self)
        self.extractButton.clicked.connect(self.extract)
        
    def extract(self):
        path = 'C:\\Users\\Xtal\\Desktop\\Semestre 10\\Human-Machine\\Programs\\extract_financial_interface\\'
        zipurl = self.textFile.toPlainText()
        with urlopen(zipurl) as zipresp:
            with ZipFile(BytesIO(zipresp.read())) as zfile: 
                zfile.extract('Financials Sample Data.xlsx', path)
                for fileinfo in zfile.infolist():
                    file_name = fileinfo.filename
                    file = pathlib.Path(file_name).name
                    if file.endswith('.xlsx'): file = file
        
        filename = path + file
        df = pd.read_excel(filename)
        df = df.head(15)
        self.table.setRowCount(df.shape[0])
        self.table.setColumnCount(df.shape[1])
        self.table.setHorizontalHeaderLabels(df.columns)
        
        for rindex, row in df.iterrows():
            for cindex, value in enumerate(row):
                self.table.setItem(rindex, cindex, QtWidgets.QTableWidgetItem(str(value)))  

        output_filename = path + 'extracto.xlsx'
        if output_filename:
            df.to_excel(output_filename, index = False)
            QMessageBox.information(self, 'Saved', 'Saved File')
                            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = main()
    window.show()
    sys.exit(app.exec())