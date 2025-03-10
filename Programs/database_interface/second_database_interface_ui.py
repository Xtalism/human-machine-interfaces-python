# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'second_database_interface.ui'
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
        TableScreen.resize(816, 453)
        self.centralwidget = QWidget(TableScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.returnButton = QPushButton(self.centralwidget)
        self.returnButton.setObjectName(u"returnButton")
        self.returnButton.setGeometry(QRect(680, 400, 75, 24))
        self.table = QTableWidget(self.centralwidget)
        self.table.setObjectName(u"table")
        self.table.setGeometry(QRect(50, 20, 711, 371))
        TableScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(TableScreen)

        QMetaObject.connectSlotsByName(TableScreen)
    # setupUi

    def retranslateUi(self, TableScreen):
        TableScreen.setWindowTitle(QCoreApplication.translate("TableScreen", u"MainWindow", None))
        self.returnButton.setText(QCoreApplication.translate("TableScreen", u"Return", None))
    # retranslateUi

