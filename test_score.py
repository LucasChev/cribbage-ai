from card import card
from score import *

def test_flush():
    h = [card(x) for x in [1,3,5,7]]
    f = card(9+13)
    res = score_hand(h,f)
    
    if res != 4:
        raise ValueError('Failed test_flush')
        
    f = card(9)
    res = score_hand(h,f)
    
    if res != 5:
        raise ValueError('Failed test_flush')
    
    return

# tests a run of 5
def test_12345():
    h = [card(x) for x in [0,1,2,3+13]]
    f = card(4)
    res = score_hand(h,f)
    if res != 7:
        raise ValueError('Failed test_12345')
    return

# test a double run scheme
def test_67788():
    h = [card(x) for x in [5,6,6+13,7]]
    f = card(7+13)
    res = score_hand(h,f)
    if res != 24:
        raise ValueError('Failed test_67788')
    return

#test a triple run scheme
def test_67778():
    h = [card(x) for x in [5,6,6+13,6+26]]
    f = card(7)
    res = score_hand(h,f)
    if res != 21:
        raise ValueError('Failed test_67778')
    return

def test_5555J():
    h = [card(x) for x in [10,4+13,4+26,4+39]]
    f = card(4)
    res = score_hand(h,f)
    if res != 29:
        raise ValueError('Failed test_5555J')
    return
        
def test_6789Q():
    h = [card(x) for x in [5+13,6,7,8]]
    f = card(11)
    res = score_hand(h,f)
    if res != 8:
        raise ValueError('Failed test_6789Q')
    return

def test_nub():
    h = [card(x) for x in [1+13,3,5,10]]
    f = card(7)
    res = score_hand(h,f)
    if res != 1:
        raise ValueError('Failed test_nub')
    return


test_list = [test_flush, test_12345, test_67788, test_67778, test_5555J, test_6789Q, test_nub]
for test in test_list:
    test()
