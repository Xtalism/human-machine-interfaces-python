# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'extract_zipaMPyLP.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QMainWindow, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QTextEdit,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1087, 877)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.table = QTableWidget(self.centralwidget)
        self.table.setObjectName(u"table")
        self.table.setGeometry(QRect(80, 110, 911, 701))
        self.textFile = QTextEdit(self.centralwidget)
        self.textFile.setObjectName(u"textFile")
        self.textFile.setGeometry(QRect(80, 50, 811, 41))
        self.extractButton = QPushButton(self.centralwidget)
        self.extractButton.setObjectName(u"extractButton")
        self.extractButton.setGeometry(QRect(920, 50, 75, 31))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.extractButton.setText(QCoreApplication.translate("MainWindow", u"Extract", None))
    # retranslateUi

