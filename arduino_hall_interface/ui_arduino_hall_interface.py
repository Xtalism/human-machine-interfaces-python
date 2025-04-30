# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'arduino_hall_interfaceRjJKKw.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(313, 187)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frameColor = QFrame(self.centralwidget)
        self.frameColor.setObjectName(u"frameColor")
        self.frameColor.setGeometry(QRect(60, 50, 191, 101))
        self.frameColor.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameColor.setFrameShadow(QFrame.Shadow.Raised)
        self.magnetPolarity = QLabel(self.frameColor)
        self.magnetPolarity.setObjectName(u"magnetPolarity")
        self.magnetPolarity.setGeometry(QRect(50, 40, 91, 16))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 20, 91, 16))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.magnetPolarity.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Magnet Polarity", None))
    # retranslateUi

