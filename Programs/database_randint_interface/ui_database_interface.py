# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'database_interfaceMcqKwm.ui'
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
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)

class Ui_TableScreen(object):
    def setupUi(self, TableScreen):
        if not TableScreen.objectName():
            TableScreen.setObjectName(u"TableScreen")
        TableScreen.resize(746, 453)
        self.centralwidget = QWidget(TableScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.addRecord = QPushButton(self.centralwidget)
        self.addRecord.setObjectName(u"addRecord")
        self.addRecord.setGeometry(QRect(620, 410, 75, 24))
        self.table = QTableWidget(self.centralwidget)
        self.table.setObjectName(u"table")
        self.table.setGeometry(QRect(40, 20, 661, 371))
        self.maxValues = QPushButton(self.centralwidget)
        self.maxValues.setObjectName(u"maxValues")
        self.maxValues.setGeometry(QRect(50, 410, 75, 24))
        TableScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(TableScreen)

        QMetaObject.connectSlotsByName(TableScreen)
    # setupUi

    def retranslateUi(self, TableScreen):
        TableScreen.setWindowTitle(QCoreApplication.translate("TableScreen", u"MainWindow", None))
        self.addRecord.setText(QCoreApplication.translate("TableScreen", u"Register", None))
        self.maxValues.setText(QCoreApplication.translate("TableScreen", u"Max Values", None))
    # retranslateUi

