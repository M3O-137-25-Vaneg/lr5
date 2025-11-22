import pytest
from random import *
#Проверка на четность суммы цифр в числе
def sum_num(n):
    sum = 0
    for i in str(n):
        sum += int(i)
    return(sum % 2 == 0)

@pytest.mark.parametrize('x, result',
                         [(12345678, False),
                          (24644422442, True),
                          (123456789, False)])
def test_sum_num(x, result):
    assert sum_num(x) == result