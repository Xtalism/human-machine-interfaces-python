# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'arduino_ultrasonic_interface.ui'
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
    QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(377, 320)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.milimeterReading = QLCDNumber(self.centralwidget)
        self.milimeterReading.setObjectName(u"milimeterReading")
        self.milimeterReading.setGeometry(QRect(70, 50, 231, 81))
        self.inchesReading = QLCDNumber(self.centralwidget)
        self.inchesReading.setObjectName(u"inchesReading")
        self.inchesReading.setGeometry(QRect(70, 170, 231, 81))
        self.hourLabel = QLabel(self.centralwidget)
        self.hourLabel.setObjectName(u"hourLabel")
        self.hourLabel.setGeometry(QRect(160, 270, 49, 16))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.hourLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

