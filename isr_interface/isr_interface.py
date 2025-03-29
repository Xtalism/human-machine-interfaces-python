# Manuel Piña Olivas - 201060
import sys
from PyQt6 import uic
from PyQt6.QtWidgets import *
from ui_isr import Ui_MainWindow

class main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(main, self).__init__()
        uic.loadUi('isr.ui', self)
        self.pushButton.clicked.connect(self.nomina)

    def nomina(self):
        try:
            worked_hours = float(self.textEdit.toPlainText())
            pay_per_hour = float(self.textEdit_2.toPlainText())
            if worked_hours <= 40:
                normal_pay = worked_hours * pay_per_hour
                extra_time = 0
            else:
                normal_pay = 40 * pay_per_hour
                extra_time = worked_hours - 40
            if extra_time <= 15:
                extra_pay = extra_time * (2 * pay_per_hour)
            else:
                extra_hours = 15
                extra_hours_more = extra_time - 15
                extra_pay = (extra_hours * (2 * pay_per_hour)) + (extra_hours_more * (3 * pay_per_hour + 0.15 * (worked_hours * pay_per_hour)))

            subtotal = normal_pay + extra_pay
            
            if subtotal <= 8000:
                isr = 0
            elif 8001 <= subtotal <= 13500:
                isr = 0.10 * subtotal
            elif 13501 <= subtotal <= 25000:
                isr = 0.19 * subtotal
            else:
                isr = 0.22 * subtotal
            total_pay = subtotal - isr

            self.workedHours.display(worked_hours)
            self.extraTime.display(extra_time)
            self.payPerHour.display(pay_per_hour)
            self.subtotal.display(subtotal)
            self.isr.display(isr)
            self.totalPay.display(total_pay)
            
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Data is not correct: {e}')
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = main()
    dialog.show()
    sys.exit(app.exec())