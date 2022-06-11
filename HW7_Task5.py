"""
Write a function that merges integer from sorted files and returns an iterator
file1.txt:
1
3
5
file2.txt:
2
4
6
>>> list(merge_sorted_files(["1.txt", "2.txt"]))
[1, 2, 3, 4, 5, 6]
"""
from pathlib import Path
from typing import List, Union, Iterator

#we read each file from the list and add the values to an empty array. Then we return the sorted value.
def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    a = []
    for i in file_list:
        with open(i) as f:
            for line in f.readlines():
                a.append(int(line))
    return sorted(a)