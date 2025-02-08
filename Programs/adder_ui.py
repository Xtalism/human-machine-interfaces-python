# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'adder.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPlainTextEdit, QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(493, 209)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.additionButton = QPushButton(self.centralwidget)
        self.additionButton.setObjectName(u"additionButton")
        self.additionButton.setGeometry(QRect(150, 130, 75, 24))
        self.dataA = QLineEdit(self.centralwidget)
        self.dataA.setObjectName(u"dataA")
        self.dataA.setGeometry(QRect(60, 90, 113, 22))
        self.dataB = QLineEdit(self.centralwidget)
        self.dataB.setObjectName(u"dataB")
        self.dataB.setGeometry(QRect(200, 90, 113, 22))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(100, 50, 49, 16))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(230, 50, 49, 16))
        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(340, 70, 104, 71))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.additionButton.setText(QCoreApplication.translate("MainWindow", u"Addition", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Data A", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Data B", None))
    # retranslateUi

