import sqlite3
import pickle


###SearchEngine is the table name
class LocationsDB:
    def __init__(self):
        self.conn = sqlite3.connect('locations.db')
        self.c = self.conn.cursor()

    def getLocations(self, fileName: str) -> set:
        self.c.execute("SELECT LOCATIONS from SearchEngine WHERE FILE_NAME='{}'".format(fileName))
        result = self.c.fetchone()
        if result is None:
            return set()
        return pickle.loads(result[0])

    def putLocations(self, locations: dict):
        pass

    def updateLocations(self, locations: dict):
        for key in locations.keys():
            pathsTableSet = self.getLocations(key)  # returns a set of locations
            valueSearchSet = locations[key]
            valueSearchSet = valueSearchSet.union(pathsTableSet)
            valueSearchSet = pickle.dumps(valueSearchSet)
            self.c.execute("""INSERT OR IGNORE INTO SearchEngine values(?,?)""", (key, valueSearchSet))
            self.c.execute("""UPDATE SearchEngine SET LOCATIONS=? WHERE FILE_NAME=?""", (valueSearchSet, key))
            from src.main.com.SearchEngine.UserLogger.myLogger import myLogger, Level
            myLogger("SearchEngine Table updated with file:{}".format(key), Level.INFO)
        self.conn.commit()
        from src.main.com.SearchEngine.IO.OutputGenerator import OutputGenerator
        OutputGenerator.printer("Update successful!")

    def createTableFirstTimeSetup(self, tableName):
        self.c.execute('''CREATE TABLE {}(FILE_NAME text PRIMARY KEY,LOCATIONS text)'''.format(tableName))
        self.conn.commit()
        from src.main.com.SearchEngine.IO.OutputGenerator import OutputGenerator
        OutputGenerator.printer("Table {} successfully created".format(tableName))
