# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'arrange_numbers_interfaceKRdbtp.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(591, 543)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.buttonWrite = QPushButton(self.centralwidget)
        self.buttonWrite.setObjectName(u"buttonWrite")
        self.buttonWrite.setGeometry(QRect(490, 500, 75, 24))
        self.arrangedNumbers = QListWidget(self.centralwidget)
        self.arrangedNumbers.setObjectName(u"arrangedNumbers")
        self.arrangedNumbers.setGeometry(QRect(310, 80, 256, 401))
        self.randomNumbers = QListWidget(self.centralwidget)
        self.randomNumbers.setObjectName(u"randomNumbers")
        self.randomNumbers.setGeometry(QRect(30, 80, 256, 401))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 40, 101, 16))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(320, 40, 101, 16))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.buttonWrite.setText(QCoreApplication.translate("MainWindow", u"Write", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Numbers < 5000", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Numbers > 5000", None))
    # retranslateUi

