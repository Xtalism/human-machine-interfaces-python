# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'email_interfacePxWyvs.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(484, 577)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.senderText = QLineEdit(self.centralwidget)
        self.senderText.setObjectName(u"senderText")
        self.senderText.setGeometry(QRect(100, 30, 111, 22))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 30, 49, 16))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(230, 30, 49, 16))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 490, 49, 16))
        self.serverText = QLineEdit(self.centralwidget)
        self.serverText.setObjectName(u"serverText")
        self.serverText.setGeometry(QRect(90, 490, 121, 22))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 530, 49, 16))
        self.portText = QLineEdit(self.centralwidget)
        self.portText.setObjectName(u"portText")
        self.portText.setGeometry(QRect(90, 530, 61, 22))
        self.loginButton = QPushButton(self.centralwidget)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setGeometry(QRect(160, 530, 51, 24))
        self.addressText = QLineEdit(self.centralwidget)
        self.addressText.setObjectName(u"addressText")
        self.addressText.setGeometry(QRect(100, 70, 341, 22))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 70, 49, 16))
        self.titleText = QLineEdit(self.centralwidget)
        self.titleText.setObjectName(u"titleText")
        self.titleText.setGeometry(QRect(100, 110, 211, 22))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(40, 110, 49, 16))
        self.passwordText = QLineEdit(self.centralwidget)
        self.passwordText.setObjectName(u"passwordText")
        self.passwordText.setGeometry(QRect(300, 30, 141, 22))
        self.attachmentsButton = QPushButton(self.centralwidget)
        self.attachmentsButton.setObjectName(u"attachmentsButton")
        self.attachmentsButton.setGeometry(QRect(330, 110, 111, 24))
        self.message = QTextEdit(self.centralwidget)
        self.message.setObjectName(u"message")
        self.message.setGeometry(QRect(50, 160, 381, 271))
        self.sendButton = QPushButton(self.centralwidget)
        self.sendButton.setObjectName(u"sendButton")
        self.sendButton.setGeometry(QRect(360, 490, 75, 24))
        self.attachmentsLabel = QLabel(self.centralwidget)
        self.attachmentsLabel.setObjectName(u"attachmentsLabel")
        self.attachmentsLabel.setGeometry(QRect(50, 440, 381, 31))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Sender", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Server", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Port", None))
        self.loginButton.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Ttile", None))
        self.attachmentsButton.setText(QCoreApplication.translate("MainWindow", u"Attachments", None))
        self.sendButton.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.attachmentsLabel.setText("")
    # retranslateUi

