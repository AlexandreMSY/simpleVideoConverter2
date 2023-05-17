from gui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from tkinter import filedialog
from videoConverter import VideoConverter
from os import path
from pathlib import Path

currentRowSelected = 0


class Controller(Ui_MainWindow):
    def __init__(self, MainWindow):
        super().__init__(MainWindow)
        self.addButton.clicked.connect(self.__addFile)
        self.convertButton.clicked.connect(self.__convertFiles)
        self.outputFileName.textEdited.connect(self.__changeOutputFileName)
        self.tableWidget.itemClicked.connect(self.__itemClicked)
        self.__files = []
        self.__convertingQueue = []

    def __addFile(self):
        try:
            file = filedialog.askopenfilename()

            if file != "":
                fileDetails = {
                    "inputFile": file,
                    "fileName": path.basename(file),
                    "fileSize": path.getsize(file),
                    "outputName": Path(file).stem,  # https://stackoverflow.com/questions/678236/how-do-i-get-the-filename-without-the-extension-from-a-path-in-python
                }
                self.__files.append(fileDetails)

                amountOfFiles = len(self.__files)

                self.tableWidget.setRowCount(amountOfFiles)

                if amountOfFiles == 1: #in case the amount of files is 1, it sets the text of the output file name textbar as the outputName of the first file in the row
                    rowZeroOutputName = self.__files[0]["outputName"]
                    self.outputFileName.setText(rowZeroOutputName)

                # print(self.__files)

                for index, file in enumerate(self.__files):
                    fileName = file["fileName"]
                    fileSize = str(file["fileSize"])

                    print(file['outputName'])

                    self.tableWidget.setItem(index, 0, QtWidgets.QTableWidgetItem(fileName))
                    self.tableWidget.setItem(index, 1, QtWidgets.QTableWidgetItem(fileSize))

        except FileNotFoundError:
            pass

    def __convertFiles(self):
        files = self.__files
        for index, file in enumerate(files):
            conv = VideoConverter(
                inputFile=file["inputFile"],
                outputFolder="media",
                outputFileName=file["outputName"],
                options={
                    "format": "mkv",
                    "video": {"codec": "copy"},
                    "audio": {"codec": "copy"},
                },
            )

            self.__convertingQueue.append(conv)

        for item in self.__convertingQueue:
            print(item.options.keys())
            item.run()

        self.__convertingQueue.clear()

    def __changeOutputFileName(self):
        lineEditText = self.outputFileName.text()
        self.__files[currentRowSelected]["outputName"] = lineEditText

    def __itemClicked(self):
        currentRowSelected = self.tableWidget.currentRow()
        fileName = self.__files[currentRowSelected]["outputName"]

        #print(fileName)

        # print(fileName)

        outputFileName = self.outputFileName
        outputFileName.setText(fileName)
