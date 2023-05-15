from svc import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from tkinter import filedialog
from videoConverter import VideoConverter


class Controller(Ui_MainWindow):
    def __init__(self, MainWindow):
        super().__init__(MainWindow)
        self.addButton.clicked.connect(self.addFile)
        self.convertButton.clicked.connect(self.convertFiles)
        self.__files = []
        self.__convertingQueue = []

    def addFile(self):
        file = filedialog.askopenfilename()
        self.__files.append(file)

        self.tableWidget.setRowCount(len(self.__files))

        for index, item in enumerate(self.__files):
            self.tableWidget.setItem(index, 0, QtWidgets.QTableWidgetItem(item))

        """for file in self.__files:
            print(file)
            conv = VideoConverter(
                file,
                "./media/{index}.flv",
                {
                    "format": "flv",
                    "video": {"codec": "copy"},
                    "audio": {"codec": "copy"},
                },
            )

            self.__convertingQueue.append(conv)"""

        #print(self.__convertingQueue)
        #print(len(self.__convertingQueue))

    def convertFiles(self):
        for index, file in enumerate(self.__files):
           #print(file)
            #print(index)
            conv = VideoConverter(
                file,
                f"./media/{index}.flv",
                {
                    "format": "flv",
                    "video": {"codec": "copy"},
                    "audio": {"codec": "copy"},
                },
            )

            self.__convertingQueue.append(conv)
        
        """print(self.__convertingQueue)
        print(len(self.__convertingQueue))"""
        
        for index in range(0, len(self.__convertingQueue)):
            print(index)
            self.__convertingQueue[index].run()

        self.__files.clear()
