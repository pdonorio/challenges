"""
>>> helper = PaginationHelper(['a','b','c','d','e','f'], 4)
>>> helper.page_count()
2
>>> helper.item_count()
6
>>> helper.page_item_count(0)
4
>>> helper.page_item_count(1)
2
>>> helper.page_item_count(2)
-1
>>> helper.page_index(5)
1
>>> helper.page_index(2)
0
>>> helper.page_index(20)
-1
>>> helper.page_index(-10)
-1

>>> helper = PaginationHelper(['a'], 1)
>>> helper.page_index(2)
-1

>>> helper = PaginationHelper([], 4)
>>> helper.page_index(0)
-1
"""

import math


class PaginationHelper:
    def __init__(self, elements: list, page_size: int = 10):
        self._elements = elements
        self._item_count = len(self._elements)
        self._page_size = page_size
        self._page_count = math.ceil(self._item_count / self._page_size)

    def page_count(self):
        return self._page_count

    def item_count(self):
        return self._item_count

    def page_item_count(self, page: int = 0):
        if page + 1 < self._page_count:
            return self._page_size
        elif page + 1 > self._page_count:
            return -1
        return self._item_count % self._page_size

    def page_index(self, index: int = 0):
        if index >= self._item_count or index < 0 or self._item_count < 1:
            return -1
        return math.floor(index / self._page_size)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
