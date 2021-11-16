import sys
import csv
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import random

from PyQt5 import QtCore


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")

        Dialog.resize(480,360)

        Dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint)

   
        self.figure = plt.figure()

        self.canvas = FigureCanvas(self.figure)
   
        layout = QVBoxLayout()

        self.button = QPushButton('Close')

        self.button.clicked.connect(Dialog.reject)
           
        layout.addWidget(self.canvas)
           
        layout.addWidget(self.button)

        Dialog.setLayout(layout)

        time = []
        weight = []
        
        with open('weights.csv') as file:
            reader = csv.reader(file, delimiter=',')

            for row in reader:
                time.append(row[0])
                weight.append(row[1])
        
        self.figure.clear()
    
        ax = self.figure.add_subplot(111)

        import numpy as np
        np.random.seed(19680801)

    
        N = 50
        x = np.random.rand(N)
        y = np.random.rand(N)
        colors = np.random.rand(N)
        area = (30 * np.random.rand(N))**2  # 0 to 15 point radii

        plt.scatter(x, y, s=area, c=colors, alpha=0.5)
        plt.xticks(x)
        # plt.show()
    
        self.canvas.draw()

   
# driver code
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())