####################threading
# set_pid = set()
# counter = 0
# directories = []
# threads=[]
# def scanDirectory(path: str):
#     dirs = []
#     global set_pid
#     global threads
#     try:
#         #print(f"Scanning {path}+{os.getpid()}")
#         set_pid.add(os.getpid())
#         for item in os.listdir(path):
#             pathToItem = os.path.join(path, item)
#             if os.path.isdir(pathToItem):
#                 dirs.append(pathToItem)
#                 #directories.append(pathToItem)
#                 threads.append(myThread(pathToItem))
#                 threads[-1].start()
#         global counter
#         counter += (len(os.listdir(path)) - len(dirs))
#     except(PermissionError):
#         print("PermissionError opening {}".format(path))
#
# class myThread(threading.Thread):
#     def __init__(self,path):
#         threading.Thread.__init__(self)
#         self.path=path
#     def run(self):
#         scanDirectory(self.path)
#
# if __name__ == '__main__':
#     # start=time.time()
#     # scanDirectory("E:\\")
#     # for thread in threads:
#     #     thread.join()
#     # end=time.time()
#     # print("Done")
#     # print(end-start)

from src.main.com.SearchEngine.IO.OutputGenerator import OutputGenerator
from src.main.com.SearchEngine.Engine.SearchEngineV0 import SearchEngine
from src.main.com.SearchEngine.Exceptions.MyExceptions import *
from src.main.com.SearchEngine.DataBase.LocationsDB import LocationsDB
import time

if __name__ == "__main__":
    fileName = "Vaibhav Shrivastava Bank Passbook"
    #fileName = "Overwatch Launcher"
    threads = []
    SearchEngine.setFileName(fileName)
    engine = SearchEngine()
    start = time.time()
    # engine.scanDirectoryWALK("E:\\")
    engine.scanDirectoryThreader("E:\\")
    OutputGenerator.printer(FilesScanned=SearchEngine.filesScanned)
    end = time.time()
    OutputGenerator.printer(TimeElapsed=end - start)
    # if not SearchEngine.isFound:
    #     raise myFileNotFoundException(fileName)
    SearchEngine.results[fileName] = SearchEngine.result_locations
    OutputGenerator.printer(resultDict=SearchEngine.results)
    OutputGenerator.printer(SearchEngine.threadingSet)
    LocationsDB().updateLocations(SearchEngine.results)
    OutputGenerator.printer("{}:{}".format(fileName, LocationsDB().getLocations(fileName)))
