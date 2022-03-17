from collections.abc import Callable
from functools import lru_cache


def cache(func: Callable) -> Callable:
    """
 we use the decorator @lru_cache (wraps the function with the arguments passed to it
and remembers the returned result corresponding to this argument). passing the internal function,
which takes a function as an argument. Then it returns a function that has cached every call of the initial
function cached.
    """
    @lru_cache
    def inner(*args):
        return func(*args)

    return inner


# for example
# passing a function with arguments a and b
def func(a, b):
    return (a ** b) ** 2

# decorating our function
cache_func = cache(func)

some = 2, 3

val_1 = cache_func(*some)
val_2 = cache_func(*some)

assert val_1 is val_2

print(val_1)
print(val_2)