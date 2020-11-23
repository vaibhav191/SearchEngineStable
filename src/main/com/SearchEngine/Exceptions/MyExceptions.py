from src.main.com.SearchEngine.UserLogger.myLogger import *

class Error(Exception):
    pass


class PathNotFoundException(Error):  # done
    def __init__(self, path):
        self.message = "Path not found:{}".format(path)
        myLogger(self.message, Level.ERROR)

    def __str__(self):
        myLogger(self.message,Level.ERROR)
        return self.message


class myFileNotFoundException(Error):  # done
    def __init__(self, fileName):
        self.message = "File Not found:{}".format(fileName)
        myLogger(self.message, Level.ERROR)

    def __str__(self):
        myLogger(self.message, Level.ERROR)
        return self.message


class noFileToSearchException(Error):  # done
    def __init__(self):
        self.message = "Try to Set File to Search using SearchEngine.setFileName(nameFile)"
        myLogger(self.message, Level.ERROR)

    def __str__(self):
        return self.message


class InvalidLevel(Error):  # done
    def __init__(self, level: str):
        self.message = "invalid level:{}\tUse myLogger.Level enum to set valid level".format(level)
        myLogger(self.message, Level.ERROR)

    def __str__(self):
        myLogger(self.message, Level.ERROR)
        return self.message
