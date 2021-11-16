import sys
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import random

from PyQt5 import QtCore


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")

        Dialog.resize(480,320)
   
        self.figure = plt.figure()

        self.canvas = FigureCanvas(self.figure)
   
        layout = QVBoxLayout()

        self.button = QPushButton('Close')

        self.button.clicked.connect(Dialog.reject)
           
        layout.addWidget(self.canvas)
           
        layout.addWidget(self.button)
           
        Dialog.setLayout(layout)

        self.plot()
   
    
   
# driver code
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())