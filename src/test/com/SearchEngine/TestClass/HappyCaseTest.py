'''
Only Testing for test case where the search for the particular file is happening for the first time.
expected behaviour is for new search to start and store result in DB.

in the unimplemented case, the previous search result is printed and program terminates.
'''


import unittest
import sqlite3

class SearchEngineTest(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        self.conn = sqlite3.connect('locations.db')
        self.cursor = self.conn.cursor()
        from src.main.com.SearchEngine.Engine.SearchEngineV0 import SearchEngine
        self.engine = SearchEngine()
        self.fileName = 'Vaibhav Shrivastava Bank Passbook'
        self.cursor.execute("delete from SearchEngine where FILE_NAME='Vaibhav Shrivastava Bank Passbook';")
        self.conn.commit()
    @classmethod
    def tearDownClass(self) -> None:
        del(self.conn)
        del(self.cursor)

    def setUp(self) -> None:
        self.path = "E:\\"
        self.result = {'E:\\old\\6_Personal folder\\1.7_Vaibhav Documents\\Vaibhav Shrivastava Bank Passbook.pdf',
                      'E:\\1.7_Vaibhav Documents\\Vaibhav Shrivastava Bank Passbook.pdf',
                      'E:\\old\\01_DriveC\\UsersLE\\UsersLE\\6_Personal folder\\1.7_Vaibhav Documents\\Vaibhav Shrivastava Bank Passbook.pdf'}

    def tearDown(self) -> None:
        pass

    def test_a_ProvideFile(self) -> None:
        self.engine.setFileName(self.fileName)
        self.assertEqual(self.fileName, self.engine.searchFileName)
        pass

    def test_b_Searching(self) -> None:
        self.engine.scanDirectoryThreader("E:\\")
        pass

    def test_c_VerifyResult(self) -> None:
        self.assertCountEqual(self.result,self.engine.result_locations)
        pass

    def test_d_VerifyThreading(self) -> None:
        # check if threads > 1 to ensure multithreading
        self.assertGreater(len(self.engine.threadingSet), 1)
        pass

    def test_e_VerifyDataBaseStorage(self) -> None:
        # storing first
        self.engine.results[self.fileName] = self.engine.result_locations
        from src.main.com.SearchEngine.DataBase.LocationsDB import LocationsDB
        LocationsDB().updateLocations(self.engine.results)

        # retrieve and assert
        self.assertCountEqual(LocationsDB().getLocations(self.fileName), self.result)
        pass
