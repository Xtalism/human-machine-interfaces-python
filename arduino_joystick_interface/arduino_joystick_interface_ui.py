# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'arduino_joystick_interface.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QSizePolicy, QWidget)
import imagen_rc
import imagen_rc
import imagen_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 600)
        MainWindow.setMinimumSize(QSize(600, 600))
        MainWindow.setStyleSheet(u"background-color: rgb(0, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(120, 150, 351, 311))
        self.frame.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.left = QFrame(self.frame)
        self.left.setObjectName(u"left")
        self.left.setGeometry(QRect(20, 100, 111, 101))
        self.left.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(255, 0, 0);\n"
"	border-radius:50px;\n"
"}")
        self.left.setFrameShape(QFrame.Shape.NoFrame)
        self.left.setFrameShadow(QFrame.Shadow.Raised)
        self.label_6 = QLabel(self.left)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(40, 30, 31, 41))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.right = QFrame(self.frame)
        self.right.setObjectName(u"right")
        self.right.setGeometry(QRect(220, 100, 111, 101))
        self.right.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(255, 0, 0);\n"
"	border-radius:50px;\n"
"}")
        self.right.setFrameShape(QFrame.Shape.NoFrame)
        self.right.setFrameShadow(QFrame.Shadow.Raised)
        self.label_4 = QLabel(self.right)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 30, 31, 41))
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.down = QFrame(self.frame)
        self.down.setObjectName(u"down")
        self.down.setGeometry(QRect(120, 180, 111, 101))
        self.down.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(255, 0, 0);\n"
"	border-radius:50px;\n"
"}")
        self.down.setFrameShape(QFrame.Shape.NoFrame)
        self.down.setFrameShadow(QFrame.Shadow.Raised)
        self.label_5 = QLabel(self.down)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 30, 31, 41))
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.up = QFrame(self.frame)
        self.up.setObjectName(u"up")
        self.up.setGeometry(QRect(120, 20, 111, 101))
        self.up.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(255, 0, 0);\n"
"	border-radius:50px;\n"
"}")
        self.up.setFrameShape(QFrame.Shape.NoFrame)
        self.up.setFrameShadow(QFrame.Shadow.Raised)
        self.label_3 = QLabel(self.up)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 30, 31, 41))
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(150, 40, 301, 61))
        font1 = QFont()
        font1.setPointSize(26)
        font1.setBold(True)
        self.label_2.setFont(font1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"L", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"R", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"U", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"JOYSTICK TESTER", None))
    # retranslateUi

