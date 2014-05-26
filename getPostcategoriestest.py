from imports import *
from getPostcategories import getPostcategories

class TestGetPostcategories(unittest.TestCase):

    def setUp(self):
        self.db = MySQLdb.connect(host="localhost",user="root",passwd="123456",db="testdb")
        self.cur =  self.db.cursor()
        self.offset = 0
        self.limit = 5
        # db connection to a empty test database testdb

    def insertPosts(self, post_status, post_type):
        self.cur.execute("DELETE from wp_posts")
        self.cur.execute("ALTER TABLE wp_posts AUTO_INCREMENT = 1")
        self.arr = [4,230,620]          ##array with some values to insert in test database
        for i in range(3):
            rep =  " NULL , 'Hello buddy!' , 'postname1' , 'title1' , '3' , '" + post_status + "' , '" + post_type + "' , '" + str(self.arr[i]) + "' , 'open' , 'the post content' , '1' , 'abstract1' , 'extended title' , '0' , '9' , '2012-04-24 17:15:23' , '19' , '0' , 'xyz','zyz','asd'"
            sql = 'INSERT INTO wp_posts(id , post_content , post_name , post_title , post_author , post_status , post_type , post_category , comment_status , post_content_filtered , comment_count , post_abstract , post_extended_title , post_meneame_status , postrank , post_date_gmt , postrank2 , post_user_id,post_excerpt,to_ping,pinged) VALUES (%s)' %(rep)
            self.cur.execute(sql)
        self.cur.close()

    def test_getPostcategories_normalBehavior(self):
        self.insertPosts("publish", "normal") #fixture : inserting something in db for testing
        output = getPostcategories(self.db,self.offset,self.limit)     ##fetch values from table in test database
        self.assertEqual(self.arr,output)

    def test_getPostcategories_abnormalBehavior(self):
        self.insertPosts("publish", "club") #fixture : inserting something in db for testing
        output = getPostcategories(self.db,self.offset,self.limit)
        self.assertNotEqual(self.arr,output)

    def test_getPostcategories_Exception(self):
        self.assertRaises(AttributeError,getPostcategories,None,self.offset,self.limit)

    def test_getPostIds_wronglimit(self):
        self.insertPosts("publish", "normal") #fixture : inserting something in db for testing
        output = getPostcategories(self.db,self.offset,0)
        self.assertNotEqual(self.arr,output)
        
    def test_getPostIds_wrongoffset(self):
        self.insertPosts("publish", "normal") #fixture : inserting something in db for testing
        output = getPostcategories(self.db,200,self.limit)
        self.assertNotEqual(self.arr,output)
