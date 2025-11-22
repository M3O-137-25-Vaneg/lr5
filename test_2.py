import pytest
from random import *
#значение n-го числа Фибоначчи

def n_fib(n):
    n -= 2
    f1 = f2 = 1
    while n > 0:
        f1, f2 = f2, f1 + f2
        n -= 1
    return f2

def fibonacci(n):
    fib1 = fib2 = 1
    fib = [1, 1]
    for i in range(2, n):
        fib1, fib2 = fib2, fib1 + fib2
        fib.append(fib2)
    return fib

def test_n_fib():
    n = randint(1, 10000)
    l1 = fibonacci(n)
    assert n_fib(n) == l1[n-1]