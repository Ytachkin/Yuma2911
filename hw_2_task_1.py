import itertools
from typing import List, Any


def combinations(*args: List[Any]) -> List[List]:
    res = []
    #we use the analog of nested loops.
    for i in itertools.product(*args):
        #adding an item to the end of the list
        res.append(i)
    return res


print(combinations([1, 2], [3, 4]))