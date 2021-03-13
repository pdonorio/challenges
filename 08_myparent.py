"""
>>> find_children("abBA")
'AaBb'
>>> find_children("AaaaaZazzz")
'AaaaaaZzzz'
>>> find_children("CbcBcbaA")
'AaBbbCcc'
>>> find_children("xXfuUuuF")
'FfUuuuXx'
>>> find_children("")
''
"""


def find_children(partecipants: str) -> str:
    return "".join(sorted(sorted(partecipants), key=str.lower))


if __name__ == '__main__':
    import doctest

    doctest.testmod()
