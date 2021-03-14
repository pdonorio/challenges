"""
>>> solution("apples, pears # and bananas\\ngrapes\\nbananas !apples", ["#", "!"])
'apples, pears\\ngrapes\\nbananas'
>>> solution("a #b\\nc\\nd $e f g", ["#", "$"])
'a\\nc\\nd'
"""

import re


def solution(input: str, markers: list, sep: str = "\n") -> str:
    arr = []
    for row in input.split(sep):
        for marker in markers:
            row = re.sub("\\" + marker + r".*$", "", row)
        arr.append(row.rstrip())
    return sep.join(arr)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
