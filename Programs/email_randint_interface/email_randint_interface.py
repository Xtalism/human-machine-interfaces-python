import sys, smtplib, random, credentials, numpy as np
from PyQt6 import uic
from PyQt6.QtWidgets import *
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from ui_email_randint_interface import Ui_MainWindow

class main(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(main, self).__init__(parent)
        uic.loadUi('email_randint_interface.ui', self)
        self.sendButton.clicked.connect(self.generate_data)
        self.show()
        
    def generate_data(self):
        data_s = [random.randrange(0, 10000) for _ in range(1000)]
        
        minor = [str(data) for data in data_s if data < 5000]
        major = [str(data) for data in data_s if data >= 5000]

        print(f"Minors: {len(minor)}, Majors: {len(major)}")

        minorsnp = np.array([int(data) for data in minor])
        majorsnp = np.array([int(data) for data in major])

        average_minors = np.mean(minorsnp)
        variance_minors = np.var(minorsnp)
        deviationstd_minors = np.std(minorsnp)

        average_majors = np.mean(majorsnp)
        variance_majors = np.var(majorsnp)
        deviationstd_majors = np.std(majorsnp)

        self.randomNumbers.clear()
        self.arrangedNumbers.clear()

        self.randomNumbers.addItems(minor)
        self.arrangedNumbers.addItems(major)

        with open('menores.txt', 'w') as minor_txt:
            minor_txt.write(f'Variance: {variance_minors:.2f}\n')
            minor_txt.write(f'Deviation: {deviationstd_minors:.2f}\n')
            minor_txt.write(f'Average: {average_minors:.2f}\n')
            minor_txt.write('Data: \n' + '\n'.join(minor) + '\n')

        with open('mayores.txt', 'w') as major_txt:
            major_txt.write(f'Variance: {variance_majors:.2f}\n')
            major_txt.write(f'Deviation: {deviationstd_majors:.2f}\n')
            major_txt.write(f'Average: {average_majors:.2f}\n')
            major_txt.write('Data: \n' + '\n'.join(major) + '\n')
        
        self.email_login()
                
    def email_login(self):
        try:
            self.server = smtplib.SMTP('smtp.gmail.com', '587')
            self.server.ehlo()
            self.server.starttls()
            self.server.ehlo()
            self.server.login(credentials.user, credentials.password)
            
            self.sendButton.setEnabled(True)
            self.addressText.setEnabled(True)
            
            self.msg = MIMEMultipart()
            self.attachments()
            
        except smtplib.SMTPAuthenticationError:
            QMessageBox.critical(self, 'Credentials Error', 'Verify username and password')
            
        except:
            QMessageBox.critical(self, 'Server Error', 'Verify server name')
        
    def attachments(self):
        
        def open_file(file):            
            with open(file, 'rb') as attachment:
                archives = MIMEBase('application', 'octet-stream')
                archives.set_payload(attachment.read())
                encoders.encode_base64(archives)
                archives.add_header('Content-Disposition', f'attachment; filename = {file}')
                self.msg.attach(archives)
            
        open_file('mayores.txt')
        open_file('menores.txt')
        self.send_email()
                
    def send_email(self):
        response = QMessageBox.question(self, 'Send Email', 'Do you wish to send an email?',
                                        QMessageBox.StandardButton.Yes|QMessageBox.StandardButton.No)
        
        if response == QMessageBox.StandardButton.Yes:
            try:
                self.msg['From'] = credentials.user
                self.msg['To'] = self.addressText.text()
                self.msg['Subject'] = 'Random generated data'
                text = self.msg.as_string()
                self.server.sendmail(credentials.user, self.addressText.text(), text)
                QMessageBox.information(self, 'Confirmation', 'Email has been sent!')
                
            except:
                QMessageBox.critical(self, 'Error', 'Your email has not been sent!')
                            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = main()
    window.show()
    sys.exit(app.exec())