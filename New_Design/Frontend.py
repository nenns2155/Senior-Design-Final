import sys
sys.path.append('/home/pi/.local/lib/python2.7/site-packages')

import os
import subprocess
import time
import random
from crontab import CronTab
from cron_descriptor import ExpressionDescriptor

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
from PyQt5 import QtWidgets


from Main2 import Ui_MainWindow
from Feeding2 import Ui_Dialog as Ui_Feeding
from Presets2 import Ui_Dialog as Ui_Presets
from Development2 import Ui_Dialog as Ui_Development
from Weight2 import Ui_Dialog as Ui_Weight

from Backend import clearFeedings, setFeeding, Read_Voltage, setWeighing

import numpy as np

import RPi.GPIO as GPIO  # import GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(38, GPIO.OUT)
GPIO.setup(32, GPIO.OUT)


GPIO.output(32,1)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        ### Further Implementation for MainWindow
        self.Feeding.clicked.connect(self.open_Feeding)
        self.Development.clicked.connect(self.open_Development)
        self.Weight.clicked.connect(self.open_Weight)


        ### Ending Further Implementation for MainWindow      

############################################################
#Feeding Dialog
############################################################
    def open_Feeding(self):
        dialog = QtWidgets.QDialog()
        Ui_Feeding.setupUi(self, dialog)
        Ui_Feeding.retranslateUi(self, dialog)

        ### Further Implementation for Ui_Feeding
        self.Presets.clicked.connect(lambda: Clear())
        self.Add.clicked.connect(lambda: GrabValues())
        self.Add.clicked.connect(lambda: Update_List())
        

        def GrabValues():
            calories = self.spinBox.value()
            hour = self.timeEdit.time().hour()
            minute = self.timeEdit.time().minute()

            setFeeding(hour, minute ,calories)

            pass

        def Update_List():

            self.listWidget.clear()
        
            cron = CronTab(user = True)
            for job in cron:
                if str(job.comment) != "weigh":

                    temp=str(job)
                    time = temp[:temp.find('p')-1]
                    
                    if time == "@daily":
                        entry = "At Noon"
                        label = str(job.comment)
                        
                    else:
                        entry = str(ExpressionDescriptor(time))
                        label = str(job.comment)

                    self.listWidget.addItem(entry + " Feed " + str(job.comment) + " Calories")

        def Clear():
            self.listWidget.clear()
            clearFeedings()

        
        ### Ending Further Implementation for Ui_Feeding
        dialog.exec_()
        dialog.show()

    def open_Weight(self):

        dialog = QtWidgets.QDialog()
        Ui_Weight.setupUi(self, dialog)

        lambda: plot()

        def plot():
            
            # random data
            data = [random.random() for i in range(10)]
            # clearing old figure
            self.figure.clear()
            # create an axis
            ax = self.figure.add_subplot(111)
            # plot data
            ax.plot(data, '*-')
            # refresh canvas
            self.canvas.draw()

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
        Ui_Presets.retranslateUi(self, dialog)

        ### Further Implementation for Ui_Presets
        self.pushButton_1.clicked.connect(lambda: run())
        self.pushButton_2.clicked.connect(lambda: take_reading())
        self.pushButton_3.clicked.connect(lambda: setWeighing())

        def run():
            GPIO.output(38, 1)
            time.sleep(10)
            GPIO.output(38, 0)
            pass

        def take_reading():
            
            self.pushButton_2.setText(str(Read_Voltage(20)))
            
        
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
        self.Calibration.clicked.connect(lambda: take_reading())


        def take_reading():
            
            self.Calibration.setText(str(Read_Voltage(20)))
        
        ### Ending Further Implementation for Ui_Development

        dialog.exec_()
        dialog.show()
############################################################
############################################################

    def closeEvent(self, event):
        GPIO.cleanup()
        event.accept()

    
        

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
    sys.exit(app.exec_())


