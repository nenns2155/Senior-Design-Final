# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Development.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 340)
        Dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(0, 280, 461, 31))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.Calibration = QtWidgets.QPushButton(Dialog)
        self.Calibration.setGeometry(QtCore.QRect(10, 10, 201, 61))
        self.Calibration.setObjectName("Calibration")
        self.IP = QtWidgets.QPushButton(Dialog)
        self.IP.setGeometry(QtCore.QRect(10, 80, 201, 61))
        self.IP.setObjectName("IP")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Calibration.setText(_translate("Dialog", "Calibration"))
        self.IP.setText(_translate("Dialog", "Network Information"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
