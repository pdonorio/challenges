"""
# Because 3*9 = 27, 2*7 = 14, 1*4=4 and 4 has only one digit.
>>> persistence(39)
3

# Because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2
>>> persistence(999)
4

# Because 4 is already a one-digit number.
>>> persistence(4)
0


#  Python 3.8+
import math
def persistence(digit: int):
    counter = 0
    while digit >= 10:
        counter += 1
        digit = math.prod(map(int, str(digit)))
    return counter


#Python 3.6+
from operator import mul
from functools import reduce
def persistence(digit: int):
    counter = 0
    while digit >= 10:
        counter += 1
        digit = reduce(mul, map(int, str(digit)))
    return counter
"""


def multiply_digits(digit: int) -> int:
    from operator import mul
    from functools import reduce

    return reduce(mul, map(int, str(digit)))


def persistence(digit: int, counter: int = 0) -> int:
    """ recursion """
    return counter if digit < 10 else persistence(multiply_digits(digit), counter + 1)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
