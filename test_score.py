import unittest

from card import card
from score import score_hand

class test_score(unittest.TestCase):

    def test_flush_4(self):
        h = [card(x) for x in [1,3,5,7]]
        f = card(9+13)
        self.assertEqual(score_hand(h,f),4)

    def test_flush_5(self):
        h = [card(x) for x in [1,3,5,7]]
        f = card(9)
        self.assertEqual(score_hand(h,f),5)

    # tests a run of 5: (9,10,J,Q,K) = 5
    def test_910JQK(self):
        h = [card(x) for x in [8,9,11,12+13]]
        f = card(10)
        self.assertEqual(score_hand(h,f),5)

    # test a quad run scheme: (6,7,8)*4 + (7+8)*4 + (77)+(88) = 24
    def test_67788(self):
        h = [card(x) for x in [5,6,6+13,7]]
        f = card(7+13)
        self.assertEqual(score_hand(h,f),24)

    #test a triple run scheme: (6,7,8)*3 + (7+8)*3 + (777) = 21
    def test_67778(self):
        h = [card(x) for x in [5,6,6+13,6+26]]
        f = card(7)
        self.assertEqual(score_hand(h,f),21)

    # test highest scoring hand: (5+5+5)*4 + (5+J)*4 + (5555) + nub = 29
    def test_5555J(self):
        h = [card(x) for x in [10,4+13,4+26,4+39]]
        f = card(4)
        self.assertEqual(score_hand(h,f),29)
            
    # test 
    def test_6789Q(self):
        h = [card(x) for x in [5+13,6,7,8]]
        f = card(11)
        self.assertEqual(score_hand(h,f),8)

    def test_nub(self):
        h = [card(x) for x in [1+13,3,5,10]]
        f = card(7)
        self.assertEqual(score_hand(h,f),1)

    def test_5555(self):
        h = [card(x) for x in [4,4+13,4+26,4+39]]
        self.assertEqual(score_hand(h),20)

    def test_5123(self):
        h = [card(x) for x in [4+13,0,1,2]]
        self.assertEqual(score_hand(h),3)

    def test_4_card_flush(self):
        h = [card(x) for x in [1,3,5,7]]
        self.assertEqual(score_hand(h),4)

    def test_569J(self):
        h = [card(x) for x in [4+13,5,8,10]]
        self.assertEqual(score_hand(h),4)

if __name__ == '__main__':
    unittest.main()
