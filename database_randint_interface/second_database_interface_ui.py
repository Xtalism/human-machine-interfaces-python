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

class Ui_MaxValueScreen(object):
    def setupUi(self, MaxValueScreen):
        if not MaxValueScreen.objectName():
            MaxValueScreen.setObjectName(u"MaxValueScreen")
        MaxValueScreen.resize(746, 366)
        self.centralwidget = QWidget(MaxValueScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.returnButton = QPushButton(self.centralwidget)
        self.returnButton.setObjectName(u"returnButton")
        self.returnButton.setGeometry(QRect(620, 320, 75, 24))
        self.tableMaxValue = QTableWidget(self.centralwidget)
        self.tableMaxValue.setObjectName(u"tableMaxValue")
        self.tableMaxValue.setGeometry(QRect(40, 20, 661, 281))
        MaxValueScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(MaxValueScreen)

        QMetaObject.connectSlotsByName(MaxValueScreen)
    # setupUi

    def retranslateUi(self, MaxValueScreen):
        MaxValueScreen.setWindowTitle(QCoreApplication.translate("MaxValueScreen", u"MainWindow", None))
        self.returnButton.setText(QCoreApplication.translate("MaxValueScreen", u"Return", None))
    # retranslateUi

