"""
>>> snail([[1,2,3], [4,5,6], [7,8,9]])
[1, 2, 3, 6, 9, 8, 7, 4, 5]

>>> snail([[1,2,3], [8,9,4], [7,6,5]])
[1, 2, 3, 4, 5, 6, 7, 8, 9]
"""


def snail(vectors):
    path = []
    while len(vectors):
        #  a snake can snail the whole row
        path.extend(vectors.pop(0))
        # transpose + reverse = clockwise rotation
        vectors = list(zip(*vectors))[::-1]
    return path


if __name__ == '__main__':
    import doctest

    doctest.testmod()
