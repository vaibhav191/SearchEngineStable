import logging
import enum
import time

class Level(enum.Enum):
    DEBUG = 0
    INFO = 1
    WARNING = 2
    ERROR = 3
    CRITICAL = 4


class myLogger:
    def __init__(self, message, level: Level):
        logging.getLogger().setLevel(logging.DEBUG)
        localTime = time.localtime()
        self.message = message
        if level == Level.INFO:
            logging.info(self.message + "\t {}:{}:{} \t {}/{}/{}".format(localTime[3], localTime[4],
                                                                         localTime[5], localTime[2], localTime[1],
                                                                         localTime[0]))
        elif level == Level.DEBUG:
            logging.debug(self.message + "\t {}:{}:{} \t {}/{}/{}".format(localTime[3], localTime[4],
                                                                          localTime[5], localTime[2], localTime[1],
                                                                          localTime[0]))
        elif level == Level.WARNING:
            logging.warning(self.message + "\t {}:{}:{} \t {}/{}/{}".format(localTime[3], localTime[4],
                                                                            localTime[5], localTime[2], localTime[1],
                                                                            localTime[0]))
        elif level == Level.ERROR:
            logging.error(self.message + "\t {}:{}:{} \t {}/{}/{}".format(localTime[3], localTime[4],
                                                                            localTime[5], localTime[2], localTime[1],
                                                                            localTime[0]))

        elif level == Level.CRITICAL:
            logging.critical(self.message + "\t {}:{}:{} \t {}/{}/{}".format(localTime[3], localTime[4],
                                                                             localTime[5], localTime[2], localTime[1],
                                                                             localTime[0]))
        else:
            from src.main.com.SearchEngine.Exceptions.MyExceptions import InvalidLevel
            raise InvalidLevel(level)
