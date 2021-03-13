"""
>>> oneszeros([0, 0, 0, 1])
1
>>> oneszeros([0, 0, 1, 0])
2
>>> oneszeros([0, 1, 0, 1])
5
>>> oneszeros([1, 0, 0, 1])
9
>>> oneszeros([0, 0, 1, 0])
2
>>> oneszeros([0, 1, 1, 0])
6
>>> oneszeros([1, 1, 1, 1])
15
>>> oneszeros([1, 0, 1, 1])
11
"""


def oneszeros(binary_array: list) -> int:
    binary_string = "".join(str(x) for x in binary_array)
    binary_python3_string = f"0b{binary_string.lstrip('0')}"
    return int(binary_python3_string, 2)
    # return int("".join(map(str, arr)), 2)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
