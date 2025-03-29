# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lcd_add_subYXaHaX.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLCDNumber, QMainWindow,
    QSizePolicy, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(526, 288)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.inputOne = QTextEdit(self.centralwidget)
        self.inputOne.setObjectName(u"inputOne")
        self.inputOne.setGeometry(QRect(20, 20, 481, 41))
        font = QFont()
        font.setPointSize(15)
        self.inputOne.setFont(font)
        self.displayNumber = QLCDNumber(self.centralwidget)
        self.displayNumber.setObjectName(u"displayNumber")
        self.displayNumber.setGeometry(QRect(30, 130, 201, 121))
        self.boxOperation = QComboBox(self.centralwidget)
        self.boxOperation.addItem("")
        self.boxOperation.addItem("")
        self.boxOperation.setObjectName(u"boxOperation")
        self.boxOperation.setGeometry(QRect(340, 180, 111, 22))
        self.inputTwo = QTextEdit(self.centralwidget)
        self.inputTwo.setObjectName(u"inputTwo")
        self.inputTwo.setGeometry(QRect(20, 70, 481, 41))
        self.inputTwo.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.boxOperation.setItemText(0, QCoreApplication.translate("MainWindow", u"Add", None))
        self.boxOperation.setItemText(1, QCoreApplication.translate("MainWindow", u"Substract", None))

    # retranslateUi

