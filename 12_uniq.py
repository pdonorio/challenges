"""
>>> find_uniq([ 1, 1, 1, 2, 1, 1 ])
2
>>> find_uniq([ 0, 0, 0.55, 0, 0 ])
0.55
>>> find_uniq([ 3, 10, 3, 3, 3 ])
10
"""


def find_uniq(nums: list) -> int:
    """ what I focused: once you count 2 occurrences, the winner is the other """
    d = dict.fromkeys(set(nums), 0)
    for num in nums:
        d[num] += 1
        if d[num] > 1:
            d.pop(num)
            return list(d.keys())[0]

    # elegant, but in worse case it goes through the whole list:
    # a, b = set(arr)
    # return a if arr.count(a) == 1 else b


if __name__ == '__main__':
    import doctest

    doctest.testmod()
