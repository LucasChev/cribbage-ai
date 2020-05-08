from card import card
from score import *

def assert_score_hand(exp, name, hand, flop=None):
    res = -1
    if flop:
        res = score_hand(hand, flop)
    else:
        res = score_hand(hand)

    assert res == exp, ('Failed %s. Expected %d but got %d'%(name,exp,res))

def test_flush_4():
    h = [card(x) for x in [1,3,5,7]]
    f = card(9+13)
    assert_score_hand(4, 'Failed test_flush_4', h, f)

def test_flush_5():
    h = [card(x) for x in [1,3,5,7]]
    f = card(9)
    assert_score_hand(5, 'Failed test_flush_5', h, f)

# tests a run of 5: (9,10,J,Q,K) = 5
def test_910JQK():
    h = [card(x) for x in [8,9,11,12+13]]
    f = card(10)
    assert_score_hand(5, 'Failed test_910JQK', h, f)

# test a quad run scheme: (6,7,8)*4 + (7+8)*4 + (77)+(88) = 24
def test_67788():
    h = [card(x) for x in [5,6,6+13,7]]
    f = card(7+13)
    assert_score_hand(24, 'Failed test_67788', h, f)

#test a triple run scheme: (6,7,8)*3 + (7+8)*3 + (777) = 21
def test_67778():
    h = [card(x) for x in [5,6,6+13,6+26]]
    f = card(7)
    assert_score_hand(21, 'Failed test_67778', h, f)

# test highest scoring hand: (5+5+5)*4 + (5+J)*4 + (5555) + nub = 29
def test_5555J():
    h = [card(x) for x in [10,4+13,4+26,4+39]]
    f = card(4)
    assert_score_hand(29, 'Failed test_5555J', h, f)
        
# test 
def test_6789Q():
    h = [card(x) for x in [5+13,6,7,8]]
    f = card(11)
    assert_score_hand(8, 'Failed test_6789Q', h, f)

def test_nub():
    h = [card(x) for x in [1+13,3,5,10]]
    f = card(7)
    assert_score_hand(1, 'Failed test_nub', h, f)

def test_5555():
    h = [card(x) for x in [4,4+13,4+26,4+39]]
    assert_score_hand(20, 'Failed test_5555', h)

def test_5123():
    h = [card(x) for x in [4+13,0,1,2]]
    assert_score_hand(3, 'Failed test_5123', h)

def test_4_card_flush():
    h = [card(x) for x in [1,3,5,7]]
    assert_score_hand(4, 'Failed test_4_card_flush', h)

def test_569J():
    h = [card(x) for x in [4+13,4,8,10]]
    assert_score_hand(4, 'Failed test_569J', h)

def test_score():
    test_list = [test_flush_4, test_flush_5, test_910JQK, test_67788, test_67778, test_5555J, test_6789Q, test_nub,
                test_5555, test_5123, test_4_card_flush]
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

