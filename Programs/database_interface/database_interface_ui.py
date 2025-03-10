# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'database_interface.ui'
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpinBox,
    QWidget)

class Ui_RegisterScreen(object):
    def setupUi(self, RegisterScreen):
        if not RegisterScreen.objectName():
            RegisterScreen.setObjectName(u"RegisterScreen")
        RegisterScreen.resize(800, 260)
        self.centralwidget = QWidget(RegisterScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.semester = QSpinBox(self.centralwidget)
        self.semester.setObjectName(u"semester")
        self.semester.setGeometry(QRect(60, 200, 42, 22))
        self.calendar = QCalendarWidget(self.centralwidget)
        self.calendar.setObjectName(u"calendar")
        self.calendar.setGeometry(QRect(440, 30, 331, 191))
        self.name = QLineEdit(self.centralwidget)
        self.name.setObjectName(u"name")
        self.name.setGeometry(QRect(50, 40, 351, 22))
        self.surname = QLineEdit(self.centralwidget)
        self.surname.setObjectName(u"surname")
        self.surname.setGeometry(QRect(50, 90, 351, 22))
        self.address = QLineEdit(self.centralwidget)
        self.address.setObjectName(u"address")
        self.address.setGeometry(QRect(50, 140, 351, 22))
        self.seeRegister = QPushButton(self.centralwidget)
        self.seeRegister.setObjectName(u"seeRegister")
        self.seeRegister.setGeometry(QRect(320, 200, 75, 24))
        self.addRecord = QPushButton(self.centralwidget)
        self.addRecord.setObjectName(u"addRecord")
        self.addRecord.setGeometry(QRect(180, 200, 75, 24))
        self.nameLabel = QLabel(self.centralwidget)
        self.nameLabel.setObjectName(u"nameLabel")
        self.nameLabel.setGeometry(QRect(50, 20, 49, 16))
        self.surnameLabel = QLabel(self.centralwidget)
        self.surnameLabel.setObjectName(u"surnameLabel")
        self.surnameLabel.setGeometry(QRect(50, 70, 49, 16))
        self.directionLabel = QLabel(self.centralwidget)
        self.directionLabel.setObjectName(u"directionLabel")
        self.directionLabel.setGeometry(QRect(50, 120, 49, 16))
        self.semesterLabel = QLabel(self.centralwidget)
        self.semesterLabel.setObjectName(u"semesterLabel")
        self.semesterLabel.setGeometry(QRect(50, 170, 49, 16))
        RegisterScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(RegisterScreen)

        QMetaObject.connectSlotsByName(RegisterScreen)
    # setupUi

    def retranslateUi(self, RegisterScreen):
        RegisterScreen.setWindowTitle(QCoreApplication.translate("RegisterScreen", u"MainWindow", None))
        self.seeRegister.setText(QCoreApplication.translate("RegisterScreen", u"See Register", None))
        self.addRecord.setText(QCoreApplication.translate("RegisterScreen", u"Add Record", None))
        self.nameLabel.setText(QCoreApplication.translate("RegisterScreen", u"Name", None))
        self.surnameLabel.setText(QCoreApplication.translate("RegisterScreen", u"Surname", None))
        self.directionLabel.setText(QCoreApplication.translate("RegisterScreen", u"Direction", None))
        self.semesterLabel.setText(QCoreApplication.translate("RegisterScreen", u"Semester", None))
    # retranslateUi

