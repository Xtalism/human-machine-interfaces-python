# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'word_interfacednfXgM.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QSpinBox, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(446, 179)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.textName = QTextEdit(self.centralwidget)
        self.textName.setObjectName(u"textName")
        self.textName.setGeometry(QRect(100, 30, 291, 31))
        self.textCareer = QTextEdit(self.centralwidget)
        self.textCareer.setObjectName(u"textCareer")
        self.textCareer.setGeometry(QRect(100, 70, 291, 31))
        self.spinSemester = QSpinBox(self.centralwidget)
        self.spinSemester.setObjectName(u"spinSemester")
        self.spinSemester.setGeometry(QRect(100, 120, 42, 22))
        self.generateButton = QPushButton(self.centralwidget)
        self.generateButton.setObjectName(u"generateButton")
        self.generateButton.setGeometry(QRect(310, 120, 75, 24))
        self.Name = QLabel(self.centralwidget)
        self.Name.setObjectName(u"Name")
        self.Name.setGeometry(QRect(40, 40, 49, 16))
        self.Semester = QLabel(self.centralwidget)
        self.Semester.setObjectName(u"Semester")
        self.Semester.setGeometry(QRect(30, 120, 49, 16))
        self.Career = QLabel(self.centralwidget)
        self.Career.setObjectName(u"Career")
        self.Career.setGeometry(QRect(40, 80, 49, 16))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.generateButton.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.Name.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.Semester.setText(QCoreApplication.translate("MainWindow", u"Semester", None))
        self.Career.setText(QCoreApplication.translate("MainWindow", u"Career", None))
    # retranslateUi

