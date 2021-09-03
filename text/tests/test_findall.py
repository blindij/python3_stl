import pytest
import re

@pytest.fixture()
def  some_data():
    text = 'abbaaabbbbaaaa'
    pattern = 'ab'
    return re.findall(pattern,text)

def test_regex_findall(some_data):
    """ Test for fixture return a list of matched strings """
    assert some_data == ['ab','ab']
