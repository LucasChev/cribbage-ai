import unittest

from score import mark_run
from card import card

class test_run(unittest.TestCase):

    def test_run_135(self):
        arg = [card(x) for x in [0,2,4]]
        self.assertEqual(mark_run(arg),0)

    def test_run_123(self):
        arg = [card(x) for x in [0,1,2]]
        self.assertEqual(mark_run(arg),3)

    def test_run_312(self):
        arg = [card(x) for x in [2,0,1]]
        self.assertEqual(mark_run(arg),3)

    def test_run_3124(self):
        arg = [card(x) for x in [2,0,1,3]]
        self.assertEqual(mark_run(arg),4)

    def test_run_K123(self):
        arg = [card(x) for x in [12,0,1,2]]
        self.assertEqual(mark_run(arg),0)
        
    def test_run_2312(self):
        arg = [card(x) for x in [1,2,0,1+13]]
        self.assertEqual(mark_run(arg),0)
        
    def test_run_45762(self):
        arg = [card(x) for x in [3,4,6,5,1]]
        self.assertEqual(mark_run(arg),4)

    def test_run_5Q34(self):
        arg = [card(x) for x in [4,11,2,3]]
        self.assertEqual(mark_run(arg),0)  

    # TODO: make this test pass
    def test_run_123K123(self):
        arg = [card(x) for x in [0,1,2,12,0+13,1+13,2+13]]
        self.assertEqual(mark_run(arg),3)
    

if __name__ == '__main__':
    unittest.main()