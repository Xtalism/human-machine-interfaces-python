# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'isr.ui'
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
from PySide6.QtWidgets import (QApplication, QLCDNumber, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(524, 526)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.workedHours = QLCDNumber(self.centralwidget)
        self.workedHours.setObjectName(u"workedHours")
        self.workedHours.setGeometry(QRect(50, 90, 191, 61))
        self.extraTime = QLCDNumber(self.centralwidget)
        self.extraTime.setObjectName(u"extraTime")
        self.extraTime.setGeometry(QRect(50, 160, 191, 61))
        self.payPerHour = QLCDNumber(self.centralwidget)
        self.payPerHour.setObjectName(u"payPerHour")
        self.payPerHour.setGeometry(QRect(50, 230, 191, 61))
        self.subtotal = QLCDNumber(self.centralwidget)
        self.subtotal.setObjectName(u"subtotal")
        self.subtotal.setGeometry(QRect(50, 300, 191, 61))
        self.isr = QLCDNumber(self.centralwidget)
        self.isr.setObjectName(u"isr")
        self.isr.setGeometry(QRect(50, 370, 191, 61))
        self.totalPay = QLCDNumber(self.centralwidget)
        self.totalPay.setObjectName(u"totalPay")
        self.totalPay.setGeometry(QRect(50, 440, 191, 61))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(110, 40, 75, 24))
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(280, 40, 104, 31))
        self.textEdit_2 = QTextEdit(self.centralwidget)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(400, 40, 104, 31))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(290, 20, 81, 20))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(410, 20, 81, 20))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(270, 110, 91, 16))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(270, 190, 61, 16))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(270, 250, 81, 16))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(270, 320, 71, 16))
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(280, 390, 49, 16))
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(280, 460, 49, 16))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Execute", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Worked Hours", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Pay Per Hour", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Worked Hours", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Extra Hours", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Pay Per Hour", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Subtotal Pay", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"ISR", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Total Pay", None))
    # retranslateUi

