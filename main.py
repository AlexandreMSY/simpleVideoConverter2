from controller import Controller
from PyQt5 import QtCore, QtGui, QtWidgets

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Controller(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())