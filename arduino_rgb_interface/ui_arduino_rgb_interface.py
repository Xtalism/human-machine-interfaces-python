# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'arduino_rgb_interfaceijLtSm.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(501, 221)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.displayColor = QPushButton(self.centralwidget)
        self.displayColor.setObjectName(u"displayColor")
        self.displayColor.setGeometry(QRect(110, 160, 111, 24))
        self.redColor = QLineEdit(self.centralwidget)
        self.redColor.setObjectName(u"redColor")
        self.redColor.setGeometry(QRect(110, 40, 113, 22))
        self.blueColor = QLineEdit(self.centralwidget)
        self.blueColor.setObjectName(u"blueColor")
        self.blueColor.setGeometry(QRect(110, 120, 113, 22))
        self.greenColor = QLineEdit(self.centralwidget)
        self.greenColor.setObjectName(u"greenColor")
        self.greenColor.setGeometry(QRect(110, 80, 113, 22))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 50, 21, 16))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(80, 80, 21, 16))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(80, 120, 21, 16))
        self.frameColor = QFrame(self.centralwidget)
        self.frameColor.setObjectName(u"frameColor")
        self.frameColor.setGeometry(QRect(270, 40, 181, 101))
        self.frameColor.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameColor.setFrameShadow(QFrame.Shadow.Raised)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.displayColor.setText(QCoreApplication.translate("MainWindow", u"Display Color", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"R", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"G", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"B", None))
    # retranslateUi

