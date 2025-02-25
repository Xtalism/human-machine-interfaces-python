# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface_21TQciPE.ui'
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
from PySide6.QtWidgets import (QApplication, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.buttonWrite = QPushButton(self.centralwidget)
        self.buttonWrite.setObjectName(u"buttonWrite")
        self.buttonWrite.setGeometry(QRect(370, 100, 75, 24))
        self.arrangedNumbers = QListWidget(self.centralwidget)
        self.arrangedNumbers.setObjectName(u"arrangedNumbers")
        self.arrangedNumbers.setGeometry(QRect(440, 160, 256, 341))
        self.randomNumbers = QListWidget(self.centralwidget)
        self.randomNumbers.setObjectName(u"randomNumbers")
        self.randomNumbers.setGeometry(QRect(120, 160, 256, 341))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.buttonWrite.setText(QCoreApplication.translate("MainWindow", u"Write", None))
    # retranslateUi

