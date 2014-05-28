from getPostEntities import getPostEntities
from imports import *

class TestGetPostEntities(unittest.TestCase):

    def setUp(self):
        self.db = MySQLdb.connect(host="localhost",user="root",passwd="",db="testdb")
        self.cur =  self.db.cursor()

    def insertPosts(self):
        self.cur.execute("DELETE from post2entity")
        self.id = [1,2,3]
        self.entity = [1,2,3,35,67]
        self.post2entity = [ [1,2,3] , [35] , [67,1] ]
        self.cur.execute("INSERT into post2entity values (1,1),(1,2),(1,3),(2,35),(3,67),(3,1)")
        self.cur.close()

    def test_getPostEntities_normalBehavior(self):
        self.insertPosts()                                      ##fixture : inserting something in db for testing
        output1 = getPostEntities(self.db , self.id[0])         ##fetch values from table in test database corresponding to given post_id
        output2 = getPostEntities(self.db , self.id[1])         
        output3 = getPostEntities(self.db , self.id[2])         
        self.assertEqual(self.post2entity[0],output1)           ##check if input is equal to output
        self.assertEqual(self.post2entity[1],output2)
        self.assertEqual(self.post2entity[2],output3)

    def test_getPostEntities_abnormalBehavior(self):
        self.insertPosts()                                      ##fixture : inserting something in db for testing
        output = getPostEntities(self.db , 4)                   ##input a post_id to the function which has no corresponding entities
        self.assertNotEqual(random.randint(0,9999),output)         ##compare fetched entity_id to any random integer

    def test_getPostcategories_Exception(self):
        self.assertRaises(AttributeError,getPostEntities,None,random.randint(0,9999))       ##Test the database connection
