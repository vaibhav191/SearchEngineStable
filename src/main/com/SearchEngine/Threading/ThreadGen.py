import threading
import queue
from src.main.com.SearchEngine.Engine.SearchEngineV0 import SearchEngine


class MyThread(threading.Thread):
    q = queue.Queue()

    def __init__(self, path):
        super().__init__()
        self.path = path


    def run(self) -> None:
        SearchEngine().scanDirectoryThreader(self.path)
