# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Development.ui'
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Development(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 280)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(0, 280, 461, 31))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.Calibration = QtWidgets.QPushButton(Dialog)
        self.Calibration.setGeometry(QtCore.QRect(10, 10, 201, 61))
        self.Calibration.setObjectName("Calibration")
        self.IP = QtWidgets.QPushButton(Dialog)
        self.IP.setGeometry(QtCore.QRect(10, 80, 201, 61))
        self.IP.setObjectName("IP")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Calibration.setText(_translate("Dialog", "Calibration"))
        self.IP.setText(_translate("Dialog", "Network Information"))