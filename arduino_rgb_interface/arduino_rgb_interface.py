import sys
from PyQt6 import uic
from PyQt6.QtCore import pyqtSlot
from PyQt6.QtGui import QColor, QIcon
from PyQt6.QtWidgets import *
from pymata4 import pymata4

board = pymata4.Pymata4()

board.set_pin_mode_pwm_output(3)
board.set_pin_mode_pwm_output(5)
board.set_pin_mode_pwm_output(6)

class colors (QMainWindow):
    def __init__(self, parent=None):
        super(colors, self).__init__(parent)
        uic.loadUi('arduino_rgb_interface.ui', self)
        self.displayColor.clicked.connect(self.selectColor)
        
    @pyqtSlot()
    def selectColor(self):
        color = QColorDialog.getColor().getRgb()
        self.redColor.setText(str(color[0]))
        self.greenColor.setText(str(color[1]))
        self.blueColor.setText(str(color[2]))
        frame_rgb ='QFrame{background-color: rgb(' +str(color[0]) + ',' + str(color[1]) + ',' + str(color[2]) + ');}'
        self.frameColor.setStyleSheet(frame_rgb)
        
        board.pwm_write(3, color[0])
        board.pwm_write(5, color[1])
        board.pwm_write(6, color[2])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = colors()
    window.show()
    sys.exit(app.exec())