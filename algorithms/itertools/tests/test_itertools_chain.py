from itertools import *

def make_iterables_to_chain():
    yield [1,2,3]
    yield ['a', 'b', 'c']

def test_chain():
    tmp=[]
    for i in chain([1, 2, 3],['a','b','c']):
        tmp.append(  i )
    assert tmp == [ 1,2,3,'a','b','c']

def test_chain_from_iterable():
    tmp = []
    for i in chain.from_iterable(make_iterables_to_chain()):
        print (i, end=' ')
    assert tmp == True
