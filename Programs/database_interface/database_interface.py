import sys, sqlite3
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import *
from PyQt6.QtCore import QDate
from ui_database_interface import Ui_RegisterScreen
from ui_second_database_interface import Ui_TableScreen

class RegisterScreen(QMainWindow, Ui_RegisterScreen):
    def __init__(self, parent=None): 
        super(RegisterScreen, self).__init__(parent)
        uic.loadUi('database_interface.ui', self)                
        self.addRecord.clicked.connect(self.connectDB)
        self.seeRegister.clicked.connect(self.change)

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
        else: event.ignore()
        
    def change(self):
        self.hide()
        second_window = TableScreen(self)
        second_window.show()

class TableScreen(QMainWindow, Ui_TableScreen):
    def __init__(self, parent=None): 
        super(TableScreen, self).__init__(parent)
        uic.loadUi('second_database_interface.ui', self)
        self.returnButton.clicked.connect(self.change)
        conn = sqlite3.connect('database_interface.db')
        
        cur = conn.cursor()
        conn.row_factory = sqlite3.Row
        cur.execute('SELECT COUNT(*) FROM data')
        row = cur.fetchone()[0]
        
        column = conn.execute('SELECT * FROM data')
        columns = column.fetchone()
        column_number = columns.keys() # extract dictionary tags
        
        self.table.setRowCount(row)
        self.table.setColumnCount(len(column_number))
        self.table.setHorizontalHeaderLabels(column_number)
        
        cur.execute('SELECT * FROM data')
        rindex = 0
        for data in cur:
            cindex = 0
            for rdata in data:
                self.table.setItem(rindex, cindex, QtWidgets.QTableWidgetItem(str(rdata)))
                cindex += 1
            rindex += 1
            
        # for rindex = 0, data in cur:
        #     for cindex =, rdata in data:
        #         self.table.setItem(rindex, cindex, QtWidgets.QTableWidgetItem(str(rdata)))
       
    def change(self):
        self.hide()
        main_window = RegisterScreen(self)
        main_window.show()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RegisterScreen()
    window.show()
    sys.exit(app.exec())