from imports import *
from prcntagaccurcy import prcntagaccurcy

class Testpredtrain(unittest.TestCase):

    def setUp(self):
        self.array1 = [1,2,3,6]
        self.array2 = [1,2,4,4]
        
    def test_pa_normalBehavior(self):
        self.assertEqual(prcntagaccurcy(self.array1,self.array2) , 50)
