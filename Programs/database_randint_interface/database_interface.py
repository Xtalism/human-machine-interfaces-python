import sys, sqlite3, random as rm
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QApplication
from ui_database_interface import Ui_TableScreen
from ui_second_database_interface import Ui_MaxValueScreen

class TableScreen(QMainWindow, Ui_TableScreen):
    def __init__(self, parent=None):
        super(TableScreen, self).__init__(parent)
        uic.loadUi('database_interface.ui', self)
        self.addRecord.clicked.connect(self.connectDB)
        self.maxValues.clicked.connect(self.change)

    def connectDB(self):
        try:
            conn = sqlite3.connect('datosaleatorios.db')
            cur = conn.cursor()
            cur.execute('DELETE FROM data')
            
            for _ in range(100):
                random_data = rm.sample(range(0, 1000), 5)
                cur.execute('INSERT INTO data (data_1, data_2, data_3, data_4, data_5) VALUES (?, ?, ?, ?, ?)', (random_data))

            conn.commit()
            QMessageBox.information(self, 'SUCCESS', 'Data addition executed!')
            self.generateTable()

        except Exception as e:
            QMessageBox.critical(self, 'ERROR', f'Database error: {str(e)}')
        finally:
            if conn:
                cur.close()
                conn.close()

    def generateTable(self):
        try:
            conn = sqlite3.connect('datosaleatorios.db')
            cur = conn.cursor()
            conn.row_factory = sqlite3.Row

            cur.execute('SELECT COUNT(*) FROM data')
            row = cur.fetchone()[0]
            
            column = conn.execute('SELECT * FROM data')
            columns = column.fetchone()
            
            if columns:
                column_number = columns.keys()
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
            else:
                QMessageBox.information(self, 'INFO', 'No data found in the table.')

        except Exception as e:
            QMessageBox.critical(self, 'ERROR', f'Table generation error: {str(e)}')
        finally:
            if conn:
                cur.close()
                conn.close()
    
    def closeEvent(self, event):
        exitProgram(self, event)
            
    def change(self):
        self.hide()
        second_window = MaxValues(self)
        second_window.show()
        
class MaxValues(QMainWindow, Ui_MaxValueScreen):
    def __init__(self, parent=None):
        super(MaxValues, self).__init__(parent)
        uic.loadUi('second_database_interface.ui', self)
        self.returnButton.clicked.connect(self.change)
        
        conn = sqlite3.connect('datosaleatorios.db')
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        
        cur.execute('SELECT * FROM data')
        columns = cur.fetchone()
        
        column_number = columns.keys()
        self.tableMaxValue.setRowCount(5)
        self.tableMaxValue.setColumnCount(len(column_number))
        self.tableMaxValue.setHorizontalHeaderLabels(column_number)
        
        data_column = ['data_1', 'data_2', 'data_3', 'data_4', 'data_5']
        
        for col_index, column in enumerate(data_column):
            cur.execute(f'SELECT {column} FROM data ORDER BY {column} DESC LIMIT 5')
            rows = cur.fetchall()
            
            for row_index, row in enumerate(rows):
                self.tableMaxValue.setItem(row_index, col_index, QtWidgets.QTableWidgetItem(str(row[0])))
        
        cur.close()
        conn.close()
        
    def change(self):
        self.hide()
        second_window = TableScreen(self)
        second_window.show()
    
    def closeEvent(self, event):
        exitProgram(self, event)
        
def exitProgram(self, event):
    response = QMessageBox.question(self, 'Close application', 'Do you wish to close the application?', 
                                    QMessageBox.StandardButton.Yes|QMessageBox.StandardButton.No)
    
    if response == QMessageBox.StandardButton.Yes:
        event.accept()
        sys.exit(app.exec())
    else: event.ignore()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TableScreen()
    window.show()
    sys.exit(app.exec())