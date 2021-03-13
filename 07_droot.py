"""

# 1 + 6 = 7
>>> droot(16)
7

# 9 + 4 + 2 = 15  -->  1 + 5 = 6
>>> droot(942)
6

# 1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
>>> droot(132189)
6

# 4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2
>>> droot(493193)
2
"""


def droot(num: int) -> int:
    num = sum(int(char) for char in str(num))
    # if num < 10:
    if len(str(num)) > 1:
        return droot(num)
    return num

    # return n if n < 10 else digital_root(sum(map(int,str(n))))


if __name__ == '__main__':
    import doctest

    doctest.testmod()
