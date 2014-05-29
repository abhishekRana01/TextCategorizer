from getX import getX
from imports import *

class TestGetX(unittest.TestCase):

    def setUp(self):
        self.post_ids = [100001,100003,100002]
        self.post_entities = np.array( [ [100001,5] , [100001,6] , [100001,7] , [100003,5] ,[100002,5] , [100002,7] ])
        self.X = csr_matrix([[0,0,0,0,1,1,1] , [0,0,0,0,1,0,0] , [0,0,0,0,1,0,1]])

    def test_getX_normalBehavior(self):
        output = getX(self.post_entities , 7)
        self.assertEqual(np.array_equal(self.X.todense(),output.todense()),True)
        
    def test_getX_wrongcolumns(self):
        self.assertRaises(ValueError, getX, self.post_entities , 3)
        
    def test_getX_wrongpostentities(self):
        self.assertRaises(ValueError, getX, np.array([[0,0,0,0,1,1,1]]) , 7)
