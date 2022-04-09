"""
Write a generator that takes a number N as an input
and returns a generator that yields N FizzBuzz numbers
Definition of done:
 - function is created
 - function is properly formatted
 - function has tests
["1", "2", "fizz", "4", "buzz"]
* https://en.wikipedia.org/wiki/Fizz_buzz
"""

from typing import List, Generator


def fizzbuzz(n: int) -> Generator[str, None, None]:
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            yield str("fizzbuzz")
        elif i % 3 == 0:
            yield str("fizz")
        elif i % 5 == 0:
            yield str("buzz")
        else:
            yield str(i)

"""
     The yield expression exposes itself as a generator object. 
     This expression is used in the body of a function and causes the function to become a generator.   
"""
