"""
Given a list of integers numbers "nums".
You need to find a sub-array with length less equal to "k", with maximal sum.
The written function should return the sum of this sub-array.
Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""

from typing import List

def summa(a: List[int]) -> int:  # метод нахождения суммы
    s = 0
    for i in a:
        s += i
    return s


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:  # main method
    sum = 0
    i = 0
    x = len(nums) - k + 1  # len() Length of massive
    array = [[0 for j in range(k)] for i in range(x)]  # create clear(empty) massive
    while i < (len(nums) - k + 1):
        array[i] = nums[i:i + k]  # n[i:j] i-ый символ, j-конечный символ. Идёт вычленение из массива
        i += 1
    for i in array:  # i - element in massive (don't number)
        if summa(i) >= sum:
            sum = summa(i)
    return sum


print(find_maximal_subarray_sum([1, 3, -1, 3, 5, 3, 10, 6, 7, 1, 9, 1], 3))