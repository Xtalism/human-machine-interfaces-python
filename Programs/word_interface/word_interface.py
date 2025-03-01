import sys, random, datetime as dt, matplotlib.pyplot as plt
from docxtpl import DocxTemplate, InlineImage
from PyQt6 import uic, QtWidgets
from docx2pdf import convert
from PyQt6.QtWidgets import *
from ui_word_interface import Ui_MainWindow

class main(QMainWindow, Ui_MainWindow):
    def __init__(self): 
        super(main, self).__init__()
        uic.loadUi('word_interface.ui', self)
        self.generateButton.clicked.connect(self.write_word)
                
    def write_word(self):
        doc = DocxTemplate('template.docx')
        table = []
        
        for i in range(10):
            table.append({'S.No': i + 1, 'data1': random.randint(1, 100), 'data2': random.randint(1, 100), 
                                         'data3': random.randint(1, 100), 'data4': random.randint(1, 100)})
        
        highest_values = [x['data1'] for x in sorted(table, key = lambda x: x['data1'], reverse = True)][0:3]
        context = {
            'nombre': self.textName.toPlainText(),
            'num_se': str(self.spinSemester.value()),
            'carrera': self.textCareer.toPlainText(),
            'tabladedatos': table,
            'mejoresdatos': highest_values
        }
        fig, ax = plt.subplots()
        ax.bar([x['S.No'] for x in table], [y['data1'] for y in table], color = 'red')
        fig.tight_layout()
        fig.savefig('Graphic-bar.png')
        context['grafica_de_datos'] = InlineImage(doc, 'Graphic-bar.png')
        doc.render(context)
        doc.save('archive.docx')
        convert('archive.docx', 'archive.pdf')
                    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = main()
    window.show()
    sys.exit(app.exec())