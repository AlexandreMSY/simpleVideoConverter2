from gui import Ui_MainWindow
from operator import itemgetter
from PyQt5 import QtCore, QtGui, QtWidgets
from tkinter import filedialog
from videoConverter import VideoConverter
from os import path
from pathlib import Path



class Controller(Ui_MainWindow):
    def __init__(self, MainWindow):
        super().__init__(MainWindow)
        self.__files = []
        self.__convertingQueue = []
        self.__actions()
        self.__currentFile = len(self.__files)
    
    def __actions(self):
        self.addButton.clicked.connect(self.__addFile)
        self.convertButton.clicked.connect(self.__convertFiles)
        self.outputFileName.textEdited.connect(self.__changeOutputFileName)
        self.tableWidget.itemClicked.connect(self.__itemClicked)
        self.videoFormats.itemClicked.connect(self.__setVideoFormat)
    
    def __getVideoFormat(self, listIndex):
        videoFormats = {
            0: 'ogg',
            1: 'avi',
            2: 'mkv',
            3: 'webm',
            4: 'flv',
            5: 'mov',
            6: 'mp4',
            7: 'mpeg',
            8: 'wmv'
        }

        return videoFormats[listIndex]

    def __addFile(self):
        try:
            file = filedialog.askopenfilename()

            if file != "":
                file_extension = path.splitext(file)
                
                fileDetails = {
                    "inputFile": file,
                    "fileName": path.basename(file),
                    "fileExtension": file_extension,
                    "fileSize": path.getsize(file),
                    "outputName": Path(file).stem,  # https://stackoverflow.com/questions/678236/how-do-i-get-the-filename-without-the-extension-from-a-path-in-python
                    "outputFormat": 'default'
                }

                self.__files.append(fileDetails)
                amountOfFiles = len(self.__files)

                self.tableWidget.setRowCount(amountOfFiles)

                if amountOfFiles == 1: #in case the amount of files is 1, it sets the text of the output file name textbar as the outputName of the first file in the row
                    rowZeroOutputName = self.__files[0]["outputName"]
                    self.outputFileName.setText(rowZeroOutputName)

                # print(self.__files)

                for index, file in enumerate(self.__files):
                    fileName, fileSize, outputFormat = itemgetter('fileName', 'fileSize', 'outputFormat')(file)

                    fileNameWidgetItem = QtWidgets.QTableWidgetItem(fileName)
                    fileSizeWidgetItem = QtWidgets.QTableWidgetItem(str(fileSize))
                    outputFormatWidgetItem = QtWidgets.QTableWidgetItem(outputFormat)

                    self.tableWidget.setItem(index, 0, fileNameWidgetItem)
                    self.tableWidget.setItem(index, 1, fileSizeWidgetItem)
                    self.tableWidget.setItem(index, 2, outputFormatWidgetItem)


        except FileNotFoundError:
            pass

    def __convertFiles(self):
        files = self.__files

        for file in files:
            inputFile, outputName, outputFormat, fileExtension = itemgetter('inputFile', 'outputName', 'outputFormat', 'fileExtension')(file)
            format = fileExtension if outputFormat == 'default' else outputFormat

            conv = VideoConverter(
                inputFile= inputFile,
                outputFolder= "media",
                outputFileName= outputName,
                options={
                    "format": format,
                    "video": {"codec": "copy"}, 
                    "audio": {"codec": "copy"} 
                },
            )

            self.__convertingQueue.append(conv)

        for item in self.__convertingQueue:
            item.run()

        self.__convertingQueue.clear()

    def __changeOutputFileName(self):
        lineEditText = self.outputFileName.text()
        self.__files[self.__currentFile]["outputName"] = lineEditText

    def __itemClicked(self):
        self.__currentFile = self.tableWidget.currentRow()
        fileName = self.__files[self.__currentFile]["outputName"]

        print(self.__currentFile)

        #print(fileName)
        #print(fileName)

        outputFileName = self.outputFileName
        outputFileName.setText(fileName)

        print(self.__files[self.__currentFile]["outputFormat"])

    def __setVideoFormat(self):
        try:
            print(self.__currentFile)
            listIndex = self.videoFormats.currentRow()
            videoFormat = self.__getVideoFormat(listIndex)

            self.__files[self.__currentFile]["outputFormat"] = videoFormat

            outputFormatWidgetItem = QtWidgets.QTableWidgetItem(videoFormat)
            self.tableWidget.setItem(self.__currentFile, 2, outputFormatWidgetItem)

            print(self.__files[self.__currentFile]["outputFormat"])
            
            #print(videoFormat)
        except IndexError:
            print('No Files!!!')