from getPostEntities import getPostEntities
from imports import *

class TestGetPostEntities(unittest.TestCase):
    
    def setUp(self):
        self.db = MySQLdb.connect(host="localhost",user=USER,passwd=PASSWORD,db=TESTDB, autocommit=True)
        self.cur =  self.db.cursor()
        self.cur.execute("DELETE from post2entity")

    def test_getPostEntities_normalBehavior(self):
        self.cur.execute("INSERT into post2entity values (1,1),(1,2),(1,3),(2,35),(3,67),(3,1)")
        self.assertEqual([1,2,3], getPostEntities(self.db , 1))
        self.assertEqual([35], getPostEntities(self.db , 2))
        self.assertEqual([67,1], getPostEntities(self.db , 3))

    def test_getPostEntities_abnormalBehavior(self):
        self.cur.execute("INSERT into post2entity values (1,1),(1,2),(1,3),(2,35),(3,67),(3,1)")
        self.assertEqual([], getPostEntities(self.db , 4))



