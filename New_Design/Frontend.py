import sys
import os
import subprocess

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
from PyQt5 import QtWidgets

from Main2 import Ui_MainWindow
from Feeding2 import Ui_Dialog as Ui_Feeding
from Presets2 import Ui_Dialog as Ui_Presets
from Development2 import Ui_Dialog as Ui_Development

from Backend import setFeeding, Calibration

import numpy as np


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        ### Further Implementation for MainWindow
        self.Feeding.clicked.connect(self.open_Feeding)
        self.Development.clicked.connect(self.open_Development)


        ### Ending Further Implementation for MainWindow      

############################################################
#Feeding Dialog
############################################################
    def open_Feeding(self):
        dialog = QtWidgets.QDialog()
        Ui_Feeding.setupUi(self, dialog)
        Ui_Feeding.retranslateUi(self, dialog)

        ### Further Implementation for Ui_Feeding
        self.Presets.clicked.connect(lambda: self.open_Presets())
        self.Add.clicked.connect(lambda: GrabValues())
        self.Add.clicked.connect(lambda: Update_List())
        

        def GrabValues():
            calories = self.spinBox.value()
            hour = self.timeEdit.time().hour()
            minute = self.timeEdit.time().minute()

            setFeeding(hour, minute ,calories)

            pass

        def Update_List():
            
            from crontab import CronTab

            ##Need to add contab job handling
            cron = CronTab(user = True)
            for job in cron:
                string = str(job.hour) + ":" + str(job.minute) + " - " + str(job.comment) + "  Calories"
                self.listWidget.insertItem(0,string)



        ### Ending Further Implementation for Ui_Feeding
        
        dialog.exec_()
        dialog.show()
############################################################
############################################################
    
############################################################
#Preset Dialog
############################################################
    def open_Presets(self):
        dialog = QtWidgets.QDialog()
        Ui_Presets.setupUi(self, dialog)
        Ui_Feeding.retranslateUi(self, dialog)

        ### Further Implementation for Ui_Presets


        
        
        ### Ending Further Implementation for Ui_Presets

        dialog.exec_()
        dialog.show()
############################################################
############################################################


############################################################
#Development Dialog
############################################################
    def open_Development(self):
        dialog = QtWidgets.QDialog()
        Ui_Development.setupUi(self, dialog)
        Ui_Development.retranslateUi(self, dialog)

        ### Further Implementation for Ui_Development
        os.system("hostname -I")
        ip = subprocess.run(['hostname','-I'], stdout=subprocess.PIPE).stdout.decode('utf-8')

        self.IP.clicked.connect(lambda: self.IP.setText(str(ip)))
        self.Calibration.clicked.connect(lambda: Calibration())


        
        
        ### Ending Further Implementation for Ui_Development

        dialog.exec_()
        dialog.show()
############################################################
############################################################

    
        

# class Feeding(QDialog, Ui_Feeding):
#     def __init__(self):
#         super().__init__()
#         self.setupUi(self)

#         ### slots and signals for mainwindow
#         self.Add.clicked.connect(self.Presets.setText("wow"))

#     def open_Presets(self):
#         print("hit")
#         dialog = QtWidgets.QDialog()
#         Ui_Presets.setupUi(self, dialog)
#         Ui_Feeding.retranslateUi(self, dialog)
#         dialog.exec_()
#         dialog.show()





if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec())
