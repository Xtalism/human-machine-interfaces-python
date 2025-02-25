# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface_15rnHNQv.ui'
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
from PySide6.QtWidgets import (QApplication, QLCDNumber, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(530, 233)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.dataA = QLineEdit(self.centralwidget)
        self.dataA.setObjectName(u"dataA")
        self.dataA.setGeometry(QRect(100, 40, 113, 22))
        self.dataB = QLineEdit(self.centralwidget)
        self.dataB.setObjectName(u"dataB")
        self.dataB.setGeometry(QRect(310, 40, 113, 22))
        self.displayNumber = QLCDNumber(self.centralwidget)
        self.displayNumber.setObjectName(u"displayNumber")
        self.displayNumber.setGeometry(QRect(170, 70, 171, 91))
        self.buttonAdd = QPushButton(self.centralwidget)
        self.buttonAdd.setObjectName(u"buttonAdd")
        self.buttonAdd.setGeometry(QRect(80, 180, 75, 24))
        self.buttonSubstract = QPushButton(self.centralwidget)
        self.buttonSubstract.setObjectName(u"buttonSubstract")
        self.buttonSubstract.setGeometry(QRect(170, 180, 75, 24))
        self.buttonMultiply = QPushButton(self.centralwidget)
        self.buttonMultiply.setObjectName(u"buttonMultiply")
        self.buttonMultiply.setGeometry(QRect(270, 180, 81, 24))
        font = QFont()
        font.setPointSize(8)
        font.setBold(False)
        self.buttonMultiply.setFont(font)
        self.buttonDivide = QPushButton(self.centralwidget)
        self.buttonDivide.setObjectName(u"buttonDivide")
        self.buttonDivide.setGeometry(QRect(370, 180, 75, 24))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.buttonAdd.setText(QCoreApplication.translate("MainWindow", u"Suma", None))
        self.buttonSubstract.setText(QCoreApplication.translate("MainWindow", u"Resta", None))
        self.buttonMultiply.setText(QCoreApplication.translate("MainWindow", u"Multiplicaci\u00f3n", None))
        self.buttonDivide.setText(QCoreApplication.translate("MainWindow", u"Divisi\u00f3n", None))
    # retranslateUi

