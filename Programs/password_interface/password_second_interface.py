import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import *
from ui_password_interface import Ui_MainWindow
from cryptography.fernet import Fernet

def load_key():
    return open('generated.key', 'rb').read()
    
class main(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(main, self).__init__(parent)
        uic.loadUi('password_interface.ui', self)
        self.loginButton.clicked.connect(self.login)

    def login(self):
        count = 0
        key = load_key()
        fernet = Fernet(key)
        user = self.userText.text()
        password = self.passwordText.text()
        keys = dict()
        user_ = list()
        password_ = list()
        
        with open('password.pass', 'r') as password_file:
            lines = password_file.readlines()
            
            for line in lines:
                data = fernet.decrypt(line).decode()
                count += 1
                
                if count %2 == 0: password_.append(data)
                else: user_.append(data)
                
            i = 0
            for i in user_:
                keys[i] = None
                keys.update(zip(keys, password_))
                
            if user in keys and keys[user] == password:
                QMessageBox.information(self, 'Correct password!', 'Correct password!')
            else:
                QMessageBox.information(self, 'Incorrect password!', 'Incorrect password!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = main()
    dialog.show()
    sys.exit(app.exec())