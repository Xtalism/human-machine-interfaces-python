# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'email_randint_interfaceJcfCHZ.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QPushButton, QSizePolicy,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(638, 620)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.addressText = QLineEdit(self.centralwidget)
        self.addressText.setObjectName(u"addressText")
        self.addressText.setGeometry(QRect(160, 30, 341, 22))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(100, 30, 49, 16))
        self.sendButton = QPushButton(self.centralwidget)
        self.sendButton.setObjectName(u"sendButton")
        self.sendButton.setGeometry(QRect(510, 560, 75, 24))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(340, 100, 101, 16))
        self.randomNumbers = QListWidget(self.centralwidget)
        self.randomNumbers.setObjectName(u"randomNumbers")
        self.randomNumbers.setGeometry(QRect(50, 140, 256, 401))
        self.arrangedNumbers = QListWidget(self.centralwidget)
        self.arrangedNumbers.setObjectName(u"arrangedNumbers")
        self.arrangedNumbers.setGeometry(QRect(330, 140, 256, 401))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 100, 101, 16))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.sendButton.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Numbers > 5000", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Numbers < 5000", None))
    # retranslateUi

