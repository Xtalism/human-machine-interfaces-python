# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'excel_creationNqEZII.ui'
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QComboBox, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QTextEdit,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(819, 442)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.calendarWidget = QCalendarWidget(self.centralwidget)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(50, 70, 411, 281))
        self.saveButton = QPushButton(self.centralwidget)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setGeometry(QRect(720, 390, 75, 24))
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(600, 320, 69, 22))
        self.name = QTextEdit(self.centralwidget)
        self.name.setObjectName(u"name")
        self.name.setGeometry(QRect(530, 110, 151, 31))
        self.surname = QTextEdit(self.centralwidget)
        self.surname.setObjectName(u"surname")
        self.surname.setGeometry(QRect(530, 180, 151, 31))
        self.telephone = QTextEdit(self.centralwidget)
        self.telephone.setObjectName(u"telephone")
        self.telephone.setGeometry(QRect(530, 250, 151, 31))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(540, 80, 49, 16))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(540, 150, 49, 16))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(540, 220, 81, 16))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(540, 320, 41, 16))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.saveButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))

        self.label.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Surname", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Phone Number", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Group", None))
    # retranslateUi

