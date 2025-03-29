# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'password_second_interfaceuJZYGV.ui'
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
    QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(693, 84)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.userText = QLineEdit(self.centralwidget)
        self.userText.setObjectName(u"userText")
        self.userText.setGeometry(QRect(80, 30, 181, 22))
        self.passwordText = QLineEdit(self.centralwidget)
        self.passwordText.setObjectName(u"passwordText")
        self.passwordText.setGeometry(QRect(360, 30, 181, 22))
        self.passwordText.setEchoMode(QLineEdit.EchoMode.Password)
        self.generateButton = QPushButton(self.centralwidget)
        self.generateButton.setObjectName(u"generateButton")
        self.generateButton.setGeometry(QRect(570, 30, 75, 24))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 30, 49, 16))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(290, 30, 49, 16))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.generateButton.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"User", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Password", None))
    # retranslateUi

