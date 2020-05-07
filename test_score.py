from card import card
from score import *

def assert_score_hand(exp, name, hand, flop=None):
    res = score_hand(hand, flop)
    assert res == exp, ('Failed %s. Expected %d but got %d'%(name,exp,res))

def test_flush_4():
    h = [card(x) for x in [1,3,5,7]]
    f = card(9+13)
    assert_score_hand(4, 'Failed test_flush_4', h, f)

def test_flush_5():
    h = [card(x) for x in [1,3,5,7]]
    f = card(9)
    assert_score_hand(5, 'Failed test_flush_5', h, f)

# tests a run of 5
def test_12345():
    h = [card(x) for x in [0,1,2,3+13]]
    f = card(4)
    assert_score_hand(7, 'Failed test_12345', h, f)

# test a double run scheme
def test_67788():
    h = [card(x) for x in [5,6,6+13,7]]
    f = card(7+13)
    assert_score_hand(24, 'Failed test_67788', h, f)

#test a triple run scheme
def test_67778():
    h = [card(x) for x in [5,6,6+13,6+26]]
    f = card(7)
    assert_score_hand(21, 'Failed test_67778', h, f)

def test_5555J():
    h = [card(x) for x in [10,4+13,4+26,4+39]]
    f = card(4)
    assert_score_hand(29, 'Failed test_5555J', h, f)
        
def test_6789Q():
    h = [card(x) for x in [5+13,6,7,8]]
    f = card(11)
    assert_score_hand(8, 'Failed test_6789Q', h, f)

def test_nub():
    h = [card(x) for x in [1+13,3,5,10]]
    f = card(7)
    assert_score_hand(1, 'Failed test_nub', h, f)

def test_score():
    test_list = [test_flush_4,test_flush_5 , test_12345, test_67788, test_67778, test_5555J, test_6789Q, test_nub]
    err_count = 0
    for test in test_list:
        try:
            test()
        except Exception as e:
            err_count+=1
            print(e)
            
    print("Testing test_score: ran %d tests, passed %d, failed %d"%(len(test_list),
                                                                    len(test_list)-err_count,
                                                                    err_count))
            
test_score()

