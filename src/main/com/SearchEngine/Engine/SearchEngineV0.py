import os
import threading
import sys
import filecmp
import logging
import time

from src.main.com.SearchEngine.Exceptions.MyExceptions import *
from src.main.com.SearchEngine.UserLogger.myLogger import *


class SearchEngine:
    lock = threading.Lock()
    filesScanned = 0
    isFound = False
    choiceDriver = None
    threadingSet = set()
    results = dict()
    result_locations = set()
    logging.basicConfig(filename='example.log', filemode='a')
    searchFileName = ""
    First = True
    running = False
    def __init__(self):
        pass

    def setDriverToScan(self):
        drivers = self.getDrivers()
        print(*['press ' + str(i) + ' to scan ' + x + '\n' for i, x in enumerate(drivers)])
        self.choiceDriver = drivers[int(input())]

    def splitAndSetFileName(self, fileName):
        SearchEngine.searchFileName = fileName.split('.')[0]

    @staticmethod
    def setFileName(fileName):
        SearchEngine.searchFileName = fileName

    def getFileName(self):
        return self.searchFileName

    def scanDirectoryWALK(self, path: str):
        if SearchEngine.searchFileName == "":
            raise noFileToSearchException
        print("Scanning directory " + path)
        for root, dirs, files in os.walk(path):
            for file in files:
                if SearchEngine.searchFileName == file.split('.')[0]:
                    print("File Found at location:" + os.path.join(root, file))
            self.incrementFilesScanned(len(files))

    def scanDirectory(self, path: str):
        dirs = []
        for item in os.listdir(path):
            pathToItem = os.path.join(path, item)
            if os.path.isdir(pathToItem):
                dirs.append(pathToItem)
        self.incrementFilesScanned(len(os.listdir(path)) - len(dirs))
        # [self.scanDirectory(dir) for dir in dirs] // need error handling hence cant use single line code
        for dir in dirs:
            try:
                self.scanDirectory(dir)
            except(PermissionError):
                print("PermissionError opening:" + dir)

    def scanDirectoryThreader(self, path: str)->None:
        if SearchEngine.First:
            SearchEngine.First = False
            prev_result = self.checkPreviousResults()
            if len(prev_result) != 0:
                from src.main.com.SearchEngine.IO.OutputGenerator import OutputGenerator
                OutputGenerator.printer(fileName=self.searchFileName, PreviouslyFoundMatches=prev_result)
                sys.exit(1)
        running = True
        if SearchEngine.searchFileName == "":
            raise noFileToSearchException
        if not os.path.exists(path):
            raise PathNotFoundException(path)
        threads = []
        SearchEngine.threadingSet.add(threading.get_ident())
        #print("Scanning path:{}".format(path))
        try:
            for item in os.listdir(path):
                pathToItem = os.path.join(path, item)
                from src.main.com.SearchEngine.Threading.ThreadGen import MyThread
                if os.path.isdir(pathToItem):
                    threads.append(MyThread(pathToItem))
                    # dirs.append(pathToItem)
                if item.split('.')[0] == SearchEngine.searchFileName:
                    from src.main.com.SearchEngine.IO.OutputGenerator import OutputGenerator
                    #print("found at location:{}".format(pathToItem))
                    OutputGenerator.printer(FoundAtLocation=pathToItem)
                    SearchEngine.result_locations.add(pathToItem)
                    if not SearchEngine.isFound:
                        SearchEngine.isFound = True
            self.lock.acquire()
            self.incrementFilesScanned(len(os.listdir(path)) - len(threads))
            self.lock.release()
        except PermissionError:
            # localTime=time.localtime()
            myLogger("PermissionError opening " + path, Level.WARNING)

        for t in threads:
            t.start()
        for t in threads:
            t.join()
        running = False

    def setChoice(self, choice: str):
        self.choiceDriver = choice

    def getChoice(self):
        return self.choiceDriver

    @staticmethod
    def getNoFilesScanned():
        return SearchEngine.filesScanned

    def incrementFilesScanned(self, count):
        SearchEngine.filesScanned += count

    def getDrivers(self):
        drivers = [chr(x) + ':\\' for x in range(65, 91) if os.path.exists(chr(x) + ':')]
        return drivers
    def checkPreviousResults(self)->set:
        from src.main.com.SearchEngine.DataBase.LocationsDB import LocationsDB
        return LocationsDB().getLocations(self.searchFileName)