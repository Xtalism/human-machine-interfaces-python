import sys, random, numpy as np
from PyQt6 import uic
from PyQt6.QtWidgets import *
from ui_interface_21 import Ui_MainWindow

class main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(main, self).__init__()
        uic.loadUi('interface_21.ui', self)
        self.buttonWrite.clicked.connect(self.generate_data)

    def generate_data(self):
        data_s = [random.randrange(0, 10000) for _ in range(1000)]
        
        minor = [str(data) for data in data_s if data < 5000]
        major = [str(data) for data in data_s if data >= 5000]

        print(f"Minors: {len(minor)}, Majors: {len(major)}")

        minorsnp = np.array([int(data) for data in minor])
        majorsnp = np.array([int(data) for data in major])

        average_minors = np.mean(minorsnp)
        variance_minors = np.var(minorsnp)
        deviationstd_minors = np.std(minorsnp)

        average_majors = np.mean(majorsnp)
        variance_majors = np.var(majorsnp)
        deviationstd_majors = np.std(majorsnp)

        self.randomNumbers.clear()
        self.arrangedNumbers.clear()

        self.randomNumbers.addItems(minor)
        self.arrangedNumbers.addItems(major)

        with open('menores.txt', 'w') as menores_txt:
            menores_txt.write('Data: \n' + '\n'.join(minor) + '\n')
            menores_txt.write(f'Variance: {variance_minors:.2f}\n')
            menores_txt.write(f'Deviation: {deviationstd_minors:.2f}\n')
            menores_txt.write(f'Average: {average_minors:.2f}\n')

        with open('mayores.txt', 'w') as mayores_txt:
            mayores_txt.write('Data: \n' + '\n'.join(major) + '\n')
            mayores_txt.write(f'Variance: {variance_majors:.2f}\n')
            mayores_txt.write(f'Deviation: {deviationstd_majors:.2f}\n')
            mayores_txt.write(f'Average: {average_majors:.2f}\n')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = main()
    dialog.show()
    sys.exit(app.exec())