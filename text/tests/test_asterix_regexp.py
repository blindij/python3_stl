import pytest
import re

@pytest.mark.parametrize(
    "pattern,result",
    [
        ('ab*',[(0,3),(3,4),(4,8),(8,9)]),
        ('ab+',[(0,3),(4,8)]),
        ('ab?',[(0,2),(3,4),(4,6),(8,9)]),
    ],
)


def test_regex_asterix(pattern,result):
    lst = []
    text = 'abbaabbba'
    iter = re.finditer(pattern,text)
    for match in iter:
        s = match.start()
        e = match.end()
        lst.append((s,e))
    assert lst == result
