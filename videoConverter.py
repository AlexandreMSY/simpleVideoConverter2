from converter import Converter

ffmpegPath = "ffmpegFiles/ffmpeg.exe"
ffprobePath = "ffmpegFiles/ffprobe.exe"

class VideoConverter:
    def __init__(self, inputFile, outPutFile, options):
        self.__inputFile = inputFile
        self.__outPutFile = outPutFile
        self.__options = options
    
    def convert(self):
        conv = Converter(ffmpegPath, ffprobePath)
        convert = conv.convert(self.__inputFile, self.__outPutFile, self.__options)

        for timestamp in convert:
            pass

