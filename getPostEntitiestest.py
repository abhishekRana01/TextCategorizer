from getPostEntities import getPostEntities
from imports import *

class TestGetPostEntities(unittest.TestCase):
    
    def setUp(self):
        self.db = MySQLdb.connect(host="localhost",user=USER,passwd=PASSWORD,db=TESTDB, autocommit=True)
        self.cur =  self.db.cursor()
        self.cur.execute("DELETE from post2entity")
        self.post2entities = np.array( [[1,1],[1,2],[1,3],[2,35],[3,67],[3,1]])

    def test_getPostEntities_normalBehavior(self):
        self.cur.execute("INSERT into post2entity values (1,1),(1,2),(1,3),(2,35),(3,67),(3,1)")
        output = getPostEntities(self.db , [1,2,3])
        self.assertEqual(np.array_equal(output,self.post2entities),True)

    def test_getPostEntities_abnormalBehavior(self):
        self.cur.execute("INSERT into post2entity values (1,1),(1,2),(1,3),(2,35),(3,67),(3,1)")
        output = getPostEntities(self.db , [1,2])
        self.assertEqual(np.array_equal(output,self.post2entities),False)


