from imports import *
from getX import getX
from getY import getY
from train import train
from predict import predict

class Testpredtrain(unittest.TestCase):

    def setUp(self):
        self.db = MySQLdb.connect(host="localhost",user="root",passwd="123456",db="testdb")
        self.cur =  self.db.cursor()
        self.offset = 0
        self.limit = 5
        # db connection to a empty test database testdb

    def insertdiffrntPosts(self, post_status, post_type):
        self.cur.execute("DELETE from wp_posts")
        self.cur.execute("ALTER TABLE wp_posts AUTO_INCREMENT = 1")
        self.id = [1,2,3]
        self.cat = [87,87,92]
        for i in range(3):
            rep =  "'" + str(self.id[i]) + "'" + " , 'Hello buddy!' , 'postname1' , 'title1' , '3' , '" + post_status + "' , '" + post_type + "' , '" + str(self.cat[i]) + "' , 'open' , 'the post content' , '1' , 'abstract1' , 'extended title' , '0' , '9' , '2012-04-24 17:15:23' , '19' , '0' , 'xyz','zyz','asd'"
            sql = 'INSERT INTO wp_posts(id , post_content , post_name , post_title , post_author , post_status , post_type , post_category , comment_status , post_content_filtered , comment_count , post_abstract , post_extended_title , post_meneame_status , postrank , post_date_gmt , postrank2 , post_user_id,post_excerpt,to_ping,pinged) VALUES (%s)' %(rep)
            self.cur.execute(sql)
            
    def insertEntities(self):
        self.cur.execute("DELETE from post2entity")
        self.entity = [1,2,3,5,7]
        self.post2entity = [ [1,2,3] , [5] , [7,1] ]
        self.cur.execute("INSERT into post2entity values (1,1),(1,2),(1,3),(2,5),(3,7),(3,1)")
        self.X = [[0,1,1,1,0,0,0,0],[0,0,0,0,0,1,0,0],[0,1,0,0,0,0,0,1]]
        self.Y = [87,87,92]
            
    def test_tp_normalBehavior(self):
        self.insertdiffrntPosts("publish", "normal")                          ##fixture
        self.insertEntities()                                                 ##fixture

        X_temp = getX(self.db,0,20).todense().tolist()                      ## construct X_temp equal to self.X
        Y_temp = getY(self.db,0,20)                                         ## Y-temp is equal to self.Y

        X_train = []
        Y_train = []

        for i in range(1000):                                               ## repeat the same cases 1000 times
            X_train.extend(X_temp)
            Y_train.extend(Y_temp)

        X_train = csr_matrix(X_train)                                       ## convert to sparse matrix format

        train(X_train,Y_train,100)
        pred = predict(X_train,Y_train,100)                                 ## testing is done on same cases as training so as to check that predicted output is equal to output during training

        self.assertEqual(pred,Y_train)

    def test_tp_abnormalBehavior(self):
        self.insertdiffrntPosts("publish", "club")                            ##fixture
        self.insertEntities()                                                 ##fixture
        
        X_train = getX(self.db,0,20)
        Y_train = getY(self.db,0,20)
        
        self.assertRaises(ValueError,train,X_train,Y_train,100)

    def test_tp_diagonalBehavior(self):
        rows = 5000
        X_train = self.diagonal(rows)                   ## create a diagonal matrix with 10000 rows
        X_train = csr_matrix(X_train)
        Y_train = [i for i in range(1,rows+1)]          ## create corresponding categories to each row in diagonal matrix

        train(X_train,Y_train,20000)

        temp = [0]*rows
        temp[2] = 1

        X_test = csr_matrix(temp)
        Y_test = [0]

        pred = predict(X_test , Y_test , 10000)
        self.assertEqual(pred , [3])
        
    def test_tp_manualpost2entitiesBehavior(self):
        ## 3 categories are chosen,each related to two entities,cat no. 1 is realted to entiies 1 and 2,cat no. 2 is realted to entiies 4 and 5,cat no. 3 is realted to entiies 1 and 5
        ## training is done 1000 times
        ## Testing is first done with entities 1,3 and 5 which should predict cat no. 3 as it resembles most
        ## Next test case is with entities 1,2 and 3 which should resemble cat no. 1
        ## Next test case is with entities 3,4 and 5 which should resemble cat no. 2
        
        X_temp = [[1,1,0,0,0],[1,0,0,0,0],[0,0,0,1,1],[0,0,0,0,1],[1,0,0,0,1]]
        Y_temp = [1,1,2,2,3]
        
        X_train = []
        Y_train = []

        for i in range(1000):
            X_train.extend(X_temp)                                      ## repeat the same cases 1000 times
            Y_train.extend(Y_temp)                                      ## repeat the same cases 1000 times


        X_train = csr_matrix(X_train)
        
        train(X_train,Y_train,2000)

        X_test = csr_matrix([[1,0,1,0,1],[1,1,1,0,0],[0,0,1,1,1]])
        Y_test = [0]*3

        pred = predict(X_test , Y_test , 100)
        self.assertEqual(pred , [3 , 1 , 2])

    def test_tp_wrongbatchsize(self):
        self.insertdiffrntPosts("publish", "normal")                          ##fixture
        self.insertEntities()                                                 ##fixture
        
        X_train = getX(self.db,0,20)
        Y_train = getY(self.db,0,20)
                        
        self.assertRaises(ValueError,train,X_train,Y_train,0)
        
        
    def diagonal(self,rows):
        arr = [1]*rows
        mat = np.diag(np.array(arr))
        return mat
