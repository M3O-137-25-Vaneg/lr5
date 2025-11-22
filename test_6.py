import pytest
from random import *

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def test_sorting_list():
    list_1 = [randint(10, 1000) for _ in range(20)]
    list = list_1
    list.sort()
    assert bubble_sort(list_1) == list