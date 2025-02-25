import sys, pandas as pd
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import *
from ui_excel_creation import Ui_MainWindow

class main(QMainWindow, Ui_MainWindow):
    def __init__(self): 
        super(main, self).__init__()
        uic.loadUi('excel_creation.ui', self)
        self.saveButton.clicked.connect(self.create_excel)
        
    def create_excel(self):
        try:
            name = self.name.toPlainText()
            surname = self.surname.toPlainText()
            telephone = self.telephone.toPlainText()
            group = self.comboBox.currentText()
            calendar = self.calendarWidget.selectedDate().toString('yyyy-MM-dd')
            
            data = {
                'Name': [name],
                'Surname': [surname],
                'Telephone Number': [telephone],
                'Group': [group],
                'Date': [calendar]
            }
            
            df = pd.DataFrame(data)
            filename, _ =QFileDialog.getSaveFileName(self, caption='Save excel', 
                                                     filter = 'Excel file(*.xlsx)')
            if filename:
                df.to_excel(filename, index = False)
                QMessageBox.information(self, 'Saved', 'Saved File')

        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Error: {str(e)}')
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = main()
    window.show()
    sys.exit(app.exec())