import pytest
from random import *

def insert_sorting(list):
    for i in range(1, len(list)):
        j = i - 1
        insert_item = list[i]
        while j >= 0 and list[j] > insert_item:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = insert_item
    return list


def test_sorting_list():
    list_1 = [randint(10, 1000) for _ in range(20)]
    list = list_1
    list.sort()
    assert insert_sorting(list_1) == list