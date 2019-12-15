from itertools import *

def test_chain():
    tmp=[]
    for i in chain([1, 2, 3],['a','b','c']):
        tmp.append(  i )
    assert tmp == [ 1,2,3,'a','b','c']
