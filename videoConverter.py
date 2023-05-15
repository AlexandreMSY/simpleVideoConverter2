from converter import Converter

ffmpegPath = "ffmpegFiles/ffmpeg.exe"
ffprobePath = "ffmpegFiles/ffprobe.exe"


class VideoConverter(Converter):
    def __init__(
        self,
        inputFile: str,
        outputFile: str,
        options: dict,
        ffmpeg_path=ffmpegPath,
        ffprobe_path=ffprobePath,
    ):
        super().__init__(ffmpeg_path, ffprobe_path)

        self.__inputFile = inputFile
        self.__outputFile = outputFile
        self.__options = options

    @property
    def inputFile(self):
        return self.__inputFile

    @inputFile.setter
    def inputFile(self, inputFile: str):
        self.__inputFile = inputFile

    @property
    def outputFile(self):
        return self.__outputFile

    @outputFile.setter
    def outputFile(self, outputFile: str):
        self.__outputFile = outputFile

    @property
    def options(self):
        return self.__options

    @options.setter
    def options(self, options: dict):
        self.__options = options

    def run(self):
        inputFile = self.__inputFile
        outputFile = self.__outputFile
        options = self.__options

        convert = self.convert(inputFile, outputFile, options, timeout=None)

        try:
            for timestamp in convert:
                print(f'\rConverting ({timestamp:2f})')
        except AttributeError:
            print('ok')
