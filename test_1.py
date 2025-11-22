import pytest
from random import *

def palindrom(n):
    pal_n = str(n)[::-1]
    return pal_n

def test_palindrom1():
    n = 12345678987654321
    assert str(n) == palindrom(n)

def test_palindrom2():
    n = randint(1, 10**6)
    assert str(n) == palindrom(n)