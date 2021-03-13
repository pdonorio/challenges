"""
>>> non_unique(['1', '2', '3', '4', '5', '5'])
[5, 2]
>>> non_unique(['1', '1', '1', '2'])
[1, 3]
>>> non_unique(['0', '0', '0', '0', '0', '0', '0.0', '0', '0', '0'])
[0, 10]
>>> non_unique(['2', '4', '6', '8', '10', '12', '14'])
'unique'
>>> non_unique(['1', '1.25', '1.50', '1.75', '2.00', '2'])
[2, 2]
>>> non_unique(['0.25', '0.0', '0.01', '0.5', '0.50'])
[0.5, 2]
>>> non_unique(['-1.05', '1.05', '1.50', '1.5'])
[1.5, 2]
>>> non_unique([])
[]
"""
from collections import Counter


def non_unique(arr: list):
    if not arr:
        return arr
    counters = Counter(map(float, arr))
    element, counter = counters.most_common(1)[0]
    if counter == 1:
        return 'unique'
    return [int(element) if element.is_integer() else element, counter]


if __name__ == '__main__':
    import doctest

    doctest.testmod()
