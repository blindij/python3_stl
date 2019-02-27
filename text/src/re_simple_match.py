import pytest
import re

@pytest.fixture()
def some_data():
    """
    Make some arbitrary text, a search pattern and do a regular
    expression search.
    """
    pattern = 'this'
    text = 'Does this text match the pattern?'
    match = re.search(pattern,text)
    s = match.start()
    e = match.end()
    return (s,e)

def test_regex_search(some_data):
    """Test for fixutre's return data"""
    assert some_data == (5,9)
