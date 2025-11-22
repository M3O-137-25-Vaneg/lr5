import pytest
from random import *
#проверка больше ли в числе четных чем нечетных цифр
def f(n):
    cnt_ch = cnt_nch = 0
    for i in str(n):
        if int(i) % 2 == 0: cnt_ch += 1
        else: cnt_nch += 1
    return(cnt_ch > cnt_nch)

@pytest.mark.parametrize('x, result',
                         [(12345678, False),
                          (1246, True),
                          (123456789, False)])
def test_f(x, result):
    assert f(x) == result