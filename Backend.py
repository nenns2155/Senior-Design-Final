
def show_Ui(Ui, Type):
    from PyQt5 import QtCore, QtGui, QtWidgets
    import sys

    app = QtWidgets.QApplication(sys.argv)
    print(app)
    Ui = Ui()

    if Type == 1:
        Dialog = QtWidgets.QDialog()
        Ui.setupUi(Dialog)
        Dialog.show()
        sys.exit(app.exec_())
    else:
        MainWindow = QtWidgets.QMainWindow()
        Ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
    return