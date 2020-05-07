from card import card
from score import *

def assert_mark_pair(arg,exp,name):
    res = mark_pair(arg)
    assert res == exp, ('Failed %s. Expected %d but got %d'%(name,exp,res))

def test_pairs_255():
    arg = [card(x) for x in [1,4,4+13]]
    assert_mark_pair(arg,0,'test_pairs_255')

def test_pairs_22():
    arg = [card(x) for x in [1,1+13]]
    assert_mark_pair(arg,2,'test_pairs_22')

def test_pairs_2255():
    arg = [card(x) for x in [1,1+13,4,4+13]]
    assert_mark_pair(arg,2,'test_pairs_2255')

def test_pairs_2225():
    arg = [card(x) for x in [1,1+13,1+26,4+13]]
    assert_mark_pair(arg,6,'test_pairs_2225')

def test_pairs_22225555():
    arg = [card(x) for x in [1,1+13,1+26,1+39,4,4+13,4+26,4+39]]
    assert_mark_pair(arg,11,'test_pairs_22225555')

def test_mark_pair():
    test_list = [test_pairs_255, test_pairs_22,test_pairs_2255,test_pairs_2225,test_pairs_22225555]
    err_count = 0
    for test in test_list:
        try:
            test()
        except Exception as e:
            err_count+=1
            print(e)
            
    print("Testing test_mark_pair: ran %d tests, passed %d, failed %d"%(len(test_list),
                                                                        len(test_list)-err_count,
                                                                        err_count))
            
test_mark_pair()