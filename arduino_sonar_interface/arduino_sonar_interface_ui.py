# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'arduino_sonar_interface.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLCDNumber, QLabel,
    QMainWindow, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(385, 192)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.sonarReading = QLCDNumber(self.centralwidget)
        self.sonarReading.setObjectName(u"sonarReading")
        self.sonarReading.setGeometry(QRect(80, 50, 231, 81))
        self.frameColor = QFrame(self.centralwidget)
        self.frameColor.setObjectName(u"frameColor")
        self.frameColor.setGeometry(QRect(330, 150, 31, 21))
        self.frameColor.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameColor.setFrameShadow(QFrame.Shadow.Raised)
        self.distance = QLabel(self.centralwidget)
        self.distance.setObjectName(u"distance")
        self.distance.setGeometry(QRect(280, 150, 49, 16))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(150, 20, 81, 16))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.distance.setText(QCoreApplication.translate("MainWindow", u"Distance", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Distance in cm", None))
    # retranslateUi

