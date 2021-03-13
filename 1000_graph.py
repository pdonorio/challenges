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

# Time complexity = n + n + n + n + n = 5n = O(n)
# Space complexity = 2n + n + n = 4n = O(n)


def get_nodes(pairs: list) -> set:
    from functools import reduce

    return reduce(set.union, (map(set, pairs)))


def get_mapping(pairs: list) -> dict:
    mappings = dict.fromkeys(get_nodes(pairs), 0)
    for _, child in pairs:
        mappings[child] += 1
    return mappings


def get_zeros_and_ones(mappings: dict) -> (list, list):
    zeros = []
    ones = []
    for node, instances in mappings.items():
        if instances == 0:
            zeros.append(node)
        elif instances == 1:
            ones.append(node)
    return zeros, ones


def find(pairs: list) -> (list, list):
    return get_zeros_and_ones(get_mapping(pairs))


pairs = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (4, 9), (9, 11)]
print(find(pairs))
