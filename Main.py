from PyQt5 import QtCore, QtGui, QtWidgets
from Feeding import Ui_Feeding as Feeding
from Development import Ui_Development as Development
from Presets import Ui_Presets as Presets


class Ui_Main(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 320)
        MainWindow.setMinimumSize(QtCore.QSize(480, 320))
        MainWindow.setMaximumSize(QtCore.QSize(480, 320))

        font = QtGui.QFont()
        font.setFamily("8514oem")
        MainWindow.setFont(font)
        MainWindow.setWindowTitle("")
        MainWindow.setAutoFillBackground(False)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.Feeding = QtWidgets.QPushButton(self.centralwidget)
        self.Feeding.setGeometry(QtCore.QRect(50, 40, 371, 51))
        self.Feeding.setObjectName("Feeding")

        self.Weight = QtWidgets.QPushButton(self.centralwidget)
        self.Weight.setGeometry(QtCore.QRect(50, 120, 371, 51))
        self.Weight.setObjectName("Weight")

        self.Development = QtWidgets.QPushButton(self.centralwidget)
        self.Development.setGeometry(QtCore.QRect(50, 200, 371, 51))
        self.Development.setObjectName("Development")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.Feeding.clicked.connect(self.open_Feeding)
        self.Development.clicked.connect(self.open_Development)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.Feeding.setText(_translate("MainWindow", "Feeding"))
        self.Weight.setText(_translate("MainWindow", "Caloric Intake"))
        self.Development.setText(_translate("MainWindow", "Development"))

    def open_Feeding(self):
        dialog = QtWidgets.QDialog()
        Feeding.setupUi(self, dialog)
        dialog.exec_()
        dialog.show()

    def open_Development(self):
        dialog = QtWidgets.QDialog()
        Development.setupUi(self, dialog)
        dialog.exec_()
        dialog.show()

    def open_Presets(self):
        dialog = QtWidgets.QDialog()
        Presets.setupUi(self, dialog)
        dialog.exec_()
        dialog.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Main()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
