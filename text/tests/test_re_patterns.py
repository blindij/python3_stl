import pytest
import re

@pytest.fixture()
def some_data():
    text = 'abbaaabbbbaaaaa'
    pattern = 'a?'
    return re.finditer(pattern,text)

def test_regexp_pattern(some_data):
    matchlist = []
    for match in some_data:
       matchlist.append((match.start(),match.end()))
    assert matchlist == [(0,1),(1,1),(2,2),(3,4),(4,5),(5,6),(6,6),(7,7),(8,8),(9,9),(10,11),(11,12),(12,13),(13,14),(14,15),(15,15)]
    assert (10,11) in matchlist
