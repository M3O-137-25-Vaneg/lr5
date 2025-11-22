import pytest
from random import *
#Проверка является ли строка числом

def isdigit(s):
    for i in s:
        if i not in '0123456789':
            return False
    return True

@pytest.mark.parametrize('x, result',
                         [('12345', True),
                          ('1234A5', False),
                          ('ASDBDSA', False)])
def test_isdigit(x, result):
    assert  isdigit(x) == result