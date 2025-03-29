# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'extract_txtlFsflo.ui'
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
    QPlainTextEdit, QPushButton, QSizePolicy, QTextBrowser,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(825, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.filePath = QTextBrowser(self.centralwidget)
        self.filePath.setObjectName(u"filePath")
        self.filePath.setGeometry(QRect(110, 50, 601, 21))
        self.openFile = QPushButton(self.centralwidget)
        self.openFile.setObjectName(u"openFile")
        self.openFile.setGeometry(QRect(30, 50, 75, 24))
        self.text = QPlainTextEdit(self.centralwidget)
        self.text.setObjectName(u"text")
        self.text.setGeometry(QRect(110, 100, 601, 451))
        self.quantityDisplay = QLCDNumber(self.centralwidget)
        self.quantityDisplay.setObjectName(u"quantityDisplay")
        self.quantityDisplay.setGeometry(QRect(740, 120, 64, 23))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(740, 100, 81, 16))
        self.sumDisplay = QLCDNumber(self.centralwidget)
        self.sumDisplay.setObjectName(u"sumDisplay")
        self.sumDisplay.setGeometry(QRect(740, 170, 64, 23))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(740, 150, 81, 16))
        self.averageDisplay = QLCDNumber(self.centralwidget)
        self.averageDisplay.setObjectName(u"averageDisplay")
        self.averageDisplay.setGeometry(QRect(740, 220, 64, 23))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(740, 200, 81, 16))
        self.varienceDisplay = QLCDNumber(self.centralwidget)
        self.varienceDisplay.setObjectName(u"varienceDisplay")
        self.varienceDisplay.setGeometry(QRect(740, 270, 64, 23))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(740, 250, 81, 16))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.openFile.setText(QCoreApplication.translate("MainWindow", u"Open File", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Data Quantity", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Data Sum", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Data Average", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Data Varience", None))
    # retranslateUi

