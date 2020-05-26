import unittest

from card import card
from score import mark_pair

class test_pair(unittest.TestCase):

    def test_pairs_255(self):
        arg = [card(x) for x in [1,4,4+13]]
        self.assertEqual(mark_pair(arg),0)

    def test_pairs_22(self):
        arg = [card(x) for x in [1,1+13]]
        self.assertEqual(mark_pair(arg),2)

    def test_pairs_2255(self):
        arg = [card(x) for x in [1,1+13,4,4+13]]
        self.assertEqual(mark_pair(arg),2)

    def test_pairs_2225(self):
        arg = [card(x) for x in [1,1+13,1+26,4+13]]
        self.assertEqual(mark_pair(arg),6)

    def test_pairs_22225555(self):
        arg = [card(x) for x in [1,1+13,1+26,1+39,4,4+13,4+26,4+39]]
        self.assertEqual(mark_pair(arg),12)

    def test_pairs_KQJ(self):
        arg = [card(x) for x in [12,11,10]]
        self.assertEqual(mark_pair(arg),0)

if __name__ == '__main__':
    unittest.main()