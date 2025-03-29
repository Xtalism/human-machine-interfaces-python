import sys, smtplib
from PyQt6 import uic
from PyQt6.QtWidgets import *
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from ui_email_interface import Ui_MainWindow

class main(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(main, self).__init__(parent)
        uic.loadUi('email_interface.ui', self)
        self.show()
        self.loginButton.clicked.connect(self.email_login)
        self.sendButton.clicked.connect(self.send_email)
        self.attachmentsButton.clicked.connect(self.attachments)
        
    def email_login(self):
        try:
            self.server = smtplib.SMTP(self.serverText.text(), self.portText.text())
            self.server.ehlo()
            self.server.starttls()
            self.server.ehlo()
            self.server.login(self.senderText.text(), self.passwordText.text())
            
            self.senderText.setEnabled(False)
            self.passwordText.setEnabled(False)
            self.serverText.setEnabled(False)
            self.portText.setEnabled(False)
            self.loginButton.setEnabled(False)
            
            self.sendButton.setEnabled(True)
            self.attachmentsButton.setEnabled(True)
            self.addressText.setEnabled(True)
            self.titleText.setEnabled(True)
            self.message.setEnabled(True)
            
            self.msg = MIMEMultipart()
        except smtplib.SMTPAuthenticationError:
            QMessageBox.critical(self, 'Credentials Error', 'Verify username and password')
            
        except:
            QMessageBox.critical(self, 'Server Error', 'Verify server name')
        
    def attachments(self):
        filenames, _ = QFileDialog.getOpenFileNames(self, caption= 'Select File', filter= 'All Files(*.*)')
        
        if filenames !=[]:
            for filename in filenames:
                attachment = open(filename, 'rb')
                filename = filename[filename.rfind('/')+1:]
                
                archives = MIMEBase('application', 'octet-stream')
                archives.set_payload(attachment.read())
                encoders.encode_base64(archives)
                archives.add_header('Content-Disposition', f'attachment; filename = {filename}')
                self.msg.attach(archives)
                
                if not self.attachmentsLabel.text().endswith(':'):
                    self.attachmentsLabel.setText(self.attachmentsLabel.text() + ',')
                self.attachmentsLabel.setText(self.attachmentsLabel.text() + '' + filename)
                
    def send_email(self):
        response = QMessageBox.question(self, 'Send Email', 'Do you wish to send an email?',
                                        QMessageBox.StandardButton.Yes|QMessageBox.StandardButton.No)
        
        if response == QMessageBox.StandardButton.Yes:
            try:
                self.msg['From'] = self.senderText.text()
                self.msg['To'] = self.addressText.text()
                self.msg['Subject'] = self.titleText.text()
                self.msg.attach(MIMEText(self.message.toPlainText(), 'plain'))
                text = self.msg.as_string()
                self.server.sendmail(self.senderText.text(), self.addressText.text(), text)
                QMessageBox.information(self, 'Confirmation', 'Email has been sent!')
                
            except:
                QMessageBox.critical(self, 'Error', 'Your email has not been sent!')
                            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = main()
    window.show()
    sys.exit(app.exec())