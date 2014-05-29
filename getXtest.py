from getX import getX
from imports import *

class TestGetX(unittest.TestCase):

    def setUp(self):
        self.post_ids = [1,3,2]
        self.post_entities = np.array( [ [1,5] , [1,6] , [1,7] , [3,5] ,[2,5] , [2,7] ])
        self.X = csr_matrix([[0,0,0,0,1,1,1] , [0,0,0,0,1,0,0] , [0,0,0,0,1,0,1]])

    def test_getX_normalBehavior(self):
        output = getX(self.post_ids , self.post_entities , 7)
        self.assertEqual(np.array_equal(self.X.todense(),output.todense()),True)
        
    def test_getX_wrongcolumns(self):
        self.assertRaises(ValueError,getX,self.post_ids , self.post_entities , 3)
        
    def test_getX_wrongpostids(self):
        output = getX([ 1 , 2 , 3 ] , self.post_entities , 7)
        self.assertEqual(np.array_equal(self.X.todense(),output.todense()),False)

    def test_getX_wrongpostentities(self):
        self.assertRaises(ValueError,getX,self.post_ids , np.array([[0,0,0,0,1,1,1]]) , 7)
