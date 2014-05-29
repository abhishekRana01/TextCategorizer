from imports import *
from getX import getX
from train import train
from predict import predict

class Testpredtrain(unittest.TestCase):

    def setUp(self):
        self.entity = [1,2,3,5,7]
        self.post2entity = [ [1,2,3] , [5] , [7,1] ]
        self.X = [[1,1,1,0,0,0,0],[0,0,0,0,1,0,0],[1,0,0,0,0,0,1]]
        self.Y = [87,87,92]
            
    def test_tp_normalBehavior(self):
        X_temp = self.X
        Y_temp = self.Y

        X_train = []
        Y_train = []

        for i in range(1000):                                               ## repeat the same cases 1000 times
            X_train.extend(X_temp)
            Y_train.extend(Y_temp)

        X_train = csr_matrix(X_train)                                       ## convert to sparse matrix format

        train(X_train,Y_train,100)
        pred = predict(X_train,100)                                 ## testing is done on same cases as training so as to check that predicted output is equal to output during training

        self.assertEqual(pred,Y_train)

    def test_tp_abnormalBehavior(self):        
        X_train = csr_matrix([])
        Y_train = []
        self.assertRaises(ValueError,train,X_train,Y_train,100)

    def test_tp_diagonalBehavior(self):
        rows = 5000
        X_train = self.diagonal(rows)                   ## create a diagonal matrix with 5000 rows
        X_train = csr_matrix(X_train)
        Y_train = [i for i in range(1,rows+1)]          ## create corresponding categories to each row in diagonal matrix

        train(X_train,Y_train,5000)

        temp = [0]*rows
        temp[2] = 1

        X_test = csr_matrix(temp)
        
        pred = predict(X_test , 10000)
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

        for i in range(100):
            X_train.extend(X_temp)                                      ## repeat the same cases 1000 times
            Y_train.extend(Y_temp)                                      ## repeat the same cases 1000 times

        X_train = csr_matrix(X_train)
        
        train(X_train,Y_train,2000)

        X_test = csr_matrix([[1,0,1,0,1],[1,1,1,0,0],[0,0,1,1,1]])
        Y_test = [0]*3

        pred = predict(X_test , 100)
        self.assertEqual(pred , [3 , 1 , 2])

    def test_tp_wrongbatchsize(self):
        
        X_train = csr_matrix(self.X)
        Y_train = self.Y
        self.assertRaises(ValueError,train,X_train,Y_train,0)
        
        
    def diagonal(self,rows):
        arr = [1]*rows
        mat = np.diag(np.array(arr))
        return mat
