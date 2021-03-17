"""
for i in range(1, 100, 1):
    three_multiple = i % 3 == 0
    five_multiple = i % 5 == 0
    if three_multiple and five_multiple:
        print("FizzBuzz")
    elif three_multiple:
        print("Fizz")
    elif five_multiple:
        print("Buzz")
    else:
        print(i)


Suppose we have some input data describing a graph of relationships between parents and children over multiple generations. The data is formatted as a list of (parent, child) pairs, where each individual is assigned a unique integer identifier.

For example, in this diagram, 3 is a child of 1 and 2, and 5 is a child of 4:
Sample input/output (pseudodata):

parentChildPairs = [
(1, 3), (2, 3), (3, 6), (5, 6),
(5, 7), (4, 5), (4, 8), (4, 9), (9, 11)
]

Write a function that takes this data as input and returns two collections: one containing all individuals with zero known parents, and one containing all individuals with exactly one known parent.

Output may be in any order:

findNodesWithZeroAndOneParents(parentChildPairs) => [
[1, 2, 4], // Individuals with zero parents
[5, 7, 8, 9, 11] // Individuals with exactly one parent
]

n: number of pairs in the input
"""

from functools import reduce


def find_parents(pairs: list) -> dict:
    mappings = dict.fromkeys(reduce(set.union, (map(set, pairs))), 0)
    for parent, child in pairs:
        mappings[child] += 1
    return mappings


def find(pairs: list) -> (list, list):
    zeros = []
    ones = []
    for node, instances in find_parents(pairs).items():
        if instances == 0:
            zeros.append(node)
        elif instances == 1:
            ones.append(node)
    return zeros, ones


pairs = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (4, 9), (9, 11)]
print(find(pairs))
