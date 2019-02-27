import pytest
import re

@pytest.fixture()
def some_data():
    text = 'abbaaabbbbaaaa'
    pattern = 'ab'
    return re.finditer(pattern,text)

def test_regex_finditer(some_data):
    """ Test for fixture returing a iteration object of matched strings"""
    iter = some_data
    text = 'abbaaabbbbaaaa'
    for match in iter:
        s = match.start()
        e = match.end()
        assert text[s:e] == 'ab'
