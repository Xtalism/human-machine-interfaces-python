import sys, os, numpy as np
from PyQt6 import uic
from PyQt6.QtWidgets import QFileDialog, QApplication, QMainWindow, QMessageBox
from ui_interface_20 import Ui_MainWindow

class StockAnalyzer(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('interface_20.ui', self)
        self.select_file_button.clicked.connect(self.browse_file)
        self.process_button.clicked.connect(self.process_stock_data)

    def browse_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select stock data file",  
                                                    filter = "Text Files (*.txt)")
        if file_path:
            self.file_path_textedit.setPlainText(file_path)

    def process_stock_data(self):
        file_path = self.file_path_textedit.toPlainText()
        if not file_path or not os.path.exists(file_path):
            QMessageBox.warning(self, "Error", "Invalid file path.")
            return
        
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
            stock_data = {}
            for line in lines:
                parts = line.strip().split(',')
                if len(parts) < 3:
                    continue
                stock_data.setdefault(parts[0], []).append(float(parts[2]))
        
            for company, values in stock_data.items():
                report_filename = f'report_{company}.txt'
                with open(report_filename, 'w') as file:
                    file.write(f'Company Name: {company}\n'
                               f'Max Stock Value: {np.max(values)}\n'
                               f'Min Stock Value: {np.min(values)}\n'
                               f'Avg Stock Value: {np.mean(values)}\n'
                               f'Variance: {np.var(values)}\n'
                               f'Standard Deviation: {np.std(values)}\n')
            QMessageBox.information(self, "Success", "Reports generated successfully.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to process file: {e}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = StockAnalyzer()
    window.show()
    sys.exit(app.exec())