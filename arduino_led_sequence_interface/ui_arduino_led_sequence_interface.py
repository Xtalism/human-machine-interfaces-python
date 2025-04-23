# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'arduino_led_sequence_interfaceOQlNVf.ui'
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QSizePolicy,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(170, 192)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.powerOn = QPushButton(self.centralwidget)
        self.powerOn.setObjectName(u"powerOn")
        self.powerOn.setGeometry(QRect(50, 30, 75, 51))
        self.powerOff = QPushButton(self.centralwidget)
        self.powerOff.setObjectName(u"powerOff")
        self.powerOff.setGeometry(QRect(50, 100, 75, 51))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.powerOn.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.powerOff.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
    # retranslateUi

