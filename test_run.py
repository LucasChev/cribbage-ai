from score import *
from card import card

def assert_mark_run(arg,exp,name):
    res = mark_run(arg)
    if res != exp:
        raise ValueError('Failed %s. Expected %d but got %d'%(name,exp,res))
    return

def test_run_135():
    arg = [card(x) for x in [0,2,4]]
    assert_mark_run(arg,0,'test_run_135')

def test_run_123():
    arg = [card(x) for x in [0,1,2]]
    assert_mark_run(arg,3,'test_run_123')

def test_run_312():
    arg = [card(x) for x in [2,0,1]]
    assert_mark_run(arg,3,'test_run_312')

def test_run_3124():
    arg = [card(x) for x in [2,0,1,3]]
    assert_mark_run(arg,4,'test_run_3124')

def test_run_K123():
    arg = [card(x) for x in [12,0,1,2]]
    assert_mark_run(arg,0,'test_run_K123')
    
def test_run_2312():
    arg = [card(x) for x in [1,2,0,1+13]]
    assert_mark_run(arg,0,'test_run_2312')
    
def test_run_45762():
    arg = [card(x) for x in [3,4,6,5,1]]
    assert_mark_run(arg,4,'test_run_45762')
    
def test_run_123K123():
    arg = [card(x) for x in [0,1,2,12,0+13,1+13,2+13]]
    assert_mark_run(arg,3,'test_run_123K123')

def test_run_5Q34():
    arg = [card(x) for x in [4,11,2,3]]
    assert_mark_run(arg,0,'test_run_5Q34')
    
def test_mark_run():
    test_list = [test_run_135,test_run_123,test_run_312,test_run_3124,
                 test_run_K123,test_run_2312,test_run_45762,test_run_123K123,test_run_5Q34]
    err_count = 0
    for test in test_list:
        try:
            test()
        except Exception as e:
            err_count+=1
            print(e)
            
    print("Testing test_mark_run: ran %d tests, passed %d, failed %d"%(len(test_list),
                                                                       len(test_list)-err_count,
                                                                       err_count))
            
test_mark_run()