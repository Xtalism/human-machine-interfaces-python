import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import *
from ui_password_second_interface import Ui_MainWindow
from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open('generated.key', 'wb') as key_file:
        key_file.write(key)

def load_key():
    return open('generated.key', 'rb').read()
    
class main(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(main, self).__init__(parent)
        uic.loadUi('password_second_interface.ui', self)
        self.generateButton.clicked.connect(self.generate)

    def generate(self):
        write_key()
        key = load_key()
        fernet = Fernet(key)
        user = self.userText.text().encode()
        password = self.passwordText.text().encode()
        
        encrypt_user = fernet.encrypt(user)
        encrypt_password = fernet.encrypt(password)
        
        file = open('password.pass', 'wb')
        file.write(encrypt_user)
        file.write(b'\n')
        file.write(encrypt_password)
        file.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = main()
    dialog.show()
    sys.exit(app.exec())