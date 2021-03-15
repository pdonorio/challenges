"""
>>> valid_solution(
... [[5, 3, 4, 6, 7, 8, 9, 1, 2],
... [6, 7, 2, 1, 9, 5, 3, 4, 8],
... [1, 9, 8, 3, 4, 2, 5, 6, 7],
... [8, 5, 9, 7, 6, 1, 4, 2, 3],
... [4, 2, 6, 8, 5, 3, 7, 9, 1],
... [7, 1, 3, 9, 2, 4, 8, 5, 6],
... [9, 6, 1, 5, 3, 7, 2, 8, 4],
... [2, 8, 7, 4, 1, 9, 6, 3, 5],
... [3, 4, 5, 2, 8, 6, 1, 7, 9]]
... )
True
>>> valid_solution(
... [[5, 3, 4, 6, 7, 8, 9, 1, 2],
... [6, 7, 2, 1, 9, 0, 3, 4, 9],
... [1, 0, 0, 3, 4, 2, 5, 6, 0],
... [8, 5, 9, 7, 6, 1, 0, 2, 0],
... [4, 2, 6, 8, 5, 3, 7, 9, 1],
... [7, 1, 3, 9, 2, 4, 8, 5, 6],
... [9, 0, 1, 5, 3, 7, 2, 1, 4],
... [2, 8, 7, 4, 1, 9, 6, 3, 5],
... [3, 0, 0, 4, 8, 1, 1, 7, 9]]
... )
False
"""

from typing import List
from itertools import chain


def verify(blocks: List[list]) -> bool:
    for block in blocks:
        if len(set(block)) != len(block):
            return False
    return True


def generate_blocks(board):
    dividers = [(0, 3), (3, 6), (6, 9)]
    blocks = []
    for d in dividers:
        subblocks = {0: [], 1: [], 2: []}
        for arr in board[d[0] : d[1]]:
            for index, d in enumerate(dividers):
                subblocks[index].extend(arr[d[0] : d[1]])
        blocks.extend(list(subblocks.values()))
    return blocks


def valid_solution(board: List[list]) -> bool:
    if 0 in list(chain(*board)):  # check zeros: must be the first
        return False
    if not verify(board):  # horizontal
        return False
    if not verify(zip(*board)):  # vertical
        return False
    if not verify(generate_blocks(board)):  # check blocks
        return False
    return True


if __name__ == '__main__':
    import doctest

    doctest.testmod()
