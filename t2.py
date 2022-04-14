import HW5_task2
from HW5_task2 import functools


@HW5_task2.print_result
def tested_func(*args):
    """Testing text"""
    return functools.reduce(lambda x, y: x**y, args)


def testing():
    assert tested_func.__doc__ == "Testing text"
    assert tested_func.__name__ == "tested_func"
    assert tested_func(2, 3) == 8