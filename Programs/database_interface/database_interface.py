import sys, sqlite3
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import *
from PyQt6.QtCore import QDate
from ui_database_interface import Ui_RegisterScreen
from ui_second_database_interface import Ui_TableScreen

class main(QMainWindow, Ui_RegisterScreen, Ui_TableScreen):
    def __init__(self): 
        super(main, self).__init__()
        uic.loadUi('database_interface.ui', self)                
        self.addRecord.clicked.connect(self.connectDB)
                
    def connectDB(self):
        try:
            conn = sqlite3.connect('database_interface.db')
            cur = conn.cursor()
            name = self.name.text()
            surname = self.surname.text()
            address = self.address.text()
            semester = self.semester.value()
            date = QDate.toString(self.calendar.selectedDate(), 'dd-MM-yyyy')            
                            
            if not(name == '' and surname == '' and address == '') and semester !=0: 
                cur.execute('INSERT INTO data (name, surname, address, semester, date) VALUES(?,?,?,?,?)',
                            (name, surname, address, semester, date))
                conn.commit()
                QMessageBox.information(self, 'SUCCESS', 'Data addition executed!')
                cur.close()
                conn.close()
            else:
                QMessageBox.information(self, 'ERROR', 'Make sure data is not empty!')
        except:
            QMessageBox.critical(self, 'ERROR', 'Database connection unsuccessful!')
    
    def closeEvent(self, event):
        response = QMessageBox.question(self, 'Close application', 'Do you wish to close the application?', 
                                        QMessageBox.StandardButton.Yes|QMessageBox.StandardButton.No)
        
        if response == QMessageBox.StandardButton.Yes:
            event.accept()
            sys.exit(app.exec())
        else:
            event.ignore()
                        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = main()
    window.show()
    sys.exit(app.exec())