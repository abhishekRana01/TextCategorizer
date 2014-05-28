from getX import getX
from imports import *
class TestGetX(unittest.TestCase):

    def setUp(self):
        self.db = MySQLdb.connect(host="localhost",user="root",passwd="",db="testdb")
        self.cur =  self.db.cursor()
        self.offset = 0
        self.limit = 5
        # db connection to a empty test database testdb

    def insertPosts(self, post_status, post_type):
        self.cur.execute("DELETE from wp_posts")
        self.cur.execute("ALTER TABLE wp_posts AUTO_INCREMENT = 1")
        self.arr = [1,2,3]
        for i in range(3):
            rep =  str(self.arr[i]) + " , 'Hello buddy!' , 'postname1' , 'title1' , '3' , '" + post_status + "' , '" + post_type + "' , '11' , 'open' , 'the post content' , '1' , 'abstract1' , 'extended title' , '0' , '9' , '2012-04-24 17:15:23' , '19' , '0' , 'xyz','zyz','asd'"
            sql = 'INSERT INTO wp_posts(id , post_content , post_name , post_title , post_author , post_status , post_type , post_category , comment_status , post_content_filtered , comment_count , post_abstract , post_extended_title , post_meneame_status , postrank , post_date_gmt , postrank2 , post_user_id,post_excerpt,to_ping,pinged) VALUES (%s)' %(rep)
            self.cur.execute(sql)
        
    def insertEntities(self):
        self.cur.execute("DELETE from post2entity")
        self.id = [1,2,3]
        self.entity = [1,2,3,5,7]
        self.post2entity = [ [1,2,3] , [5] , [7,1] ]
        self.cur.execute("INSERT into post2entity values (1,1),(1,2),(1,3),(2,5),(3,7),(3,1)")
        self.X = [[0,1,1,1,0,0,0,0],[0,0,0,0,0,1,0,0],[0,1,0,0,0,0,0,1]]
        self.cur.close()

    def test_getX_normalBehavior(self):
        self.insertPosts("publish", "normal")                          ##fixture : inserting something in db for testing
        self.insertEntities()                                          ##fixture : inserting something in db for testing
        postids = getPostIds(self.db,self.offset,self.limit)
        output = getX(postIds)                  ##fetch values from table in test database
        output = output.todense().tolist()
        self.assertEqual(self.X,output)

    def test_getX_abnormalBehavior(self):
        self.insertPosts("publish", "club")                            ##fixture : inserting something in db for testing
        self.insertEntities()                                          ##fixture : inserting something in db for testing
        output = getX(self.db,self.offset,self.limit)                  ##fetch values from table in test database
        output = output.todense().tolist()
        self.assertNotEqual(self.X,output)

    def test_getX_wronglimit(self):
        self.insertPosts("publish", "normal")                          ##fixture : inserting something in db for testing
        self.insertEntities()                                          ##fixture : inserting something in db for testing
        output = getX(self.db,self.offset,0)                           ##fetch values from table in test database
        output = output.todense().tolist()
        self.assertNotEqual(self.X,output)

    def test_getX_wrongoffset(self):
        self.insertPosts("publish", "normal")                          ##fixture : inserting something in db for testing
        self.insertEntities()                                          ##fixture : inserting something in db for testing
        output = getX(self.db,200,self.limit)                            ##fetch values from table in test database
        output = output.todense().tolist()
        self.assertNotEqual(self.X,output)


    def test_getX_Exception(self):
        self.assertRaises(AttributeError,getX,None,self.offset,self.limit)
