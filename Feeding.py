from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Feeding(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 310)

        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(250, 280, 211, 31))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 40, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setFamily("8514oem")
        self.label.setFont(font)
        self.label.setObjectName("label")

        QtWidgets.QSpinBox.adjustSize
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        self.spinBox.setGeometry(QtCore.QRect(230, 20, 141, 71))
        self.spinBox.setFont(font)
        self.spinBox.setAccelerated(True)
        self.spinBox.setMinimum(10)
        self.spinBox.setMaximum(2000)
        self.spinBox.setSingleStep(10)
        self.spinBox.setObjectName("spinBox")

        self.timeEdit = QtWidgets.QTimeEdit(Dialog)
        self.timeEdit.setGeometry(QtCore.QRect(230, 100, 141, 71))
        self.timeEdit.setFont(font)
        self.timeEdit.setTabletTracking(False)
        self.timeEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.timeEdit.setAccelerated(True)
        self.timeEdit.setCalendarPopup(False)
        self.timeEdit.setObjectName("timeEdit")

        self.Add = QtWidgets.QPushButton(Dialog)
        self.Add.setGeometry(QtCore.QRect(380, 100, 93, 71))
        self.Add.setObjectName("Add")

        self.Presets = QtWidgets.QPushButton(Dialog)
        self.Presets.setGeometry(QtCore.QRect(165, 282, 120, 28))
        self.Presets.setObjectName("Presets")

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(100, 120, 291, 41))
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(10, 180, 461, 91))
        self.listWidget.setObjectName("listWidget")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("Dialog", "Calories?"))
        self.Add.setText(_translate("Dialog", "Add Time"))
        self.Presets.setText(_translate("Dialog", "Preset Options"))
        self.label_2.setText(_translate("Dialog", "Feeding Time?"))

        self.Add.clicked.connect(lambda: self.Add.setText("WOW"))
        self.Presets.clicked.connect(self.open_Presets)
