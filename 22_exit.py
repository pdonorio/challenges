"""
>>> path_finder("\\n".join([ ".W.", ".W.", "..." ]))
True
>>> path_finder("\\n".join([ ".W.", ".W.", "W.." ]))
False
>>> path_finder("\\n".join([ "......", "......", "......", "......", "......", "......" ]))
True
>>> path_finder("\\n".join([ "......", "......", "......", "......", ".....W", "....W." ]))
False
>>> path_finder("\\n".join([]))
False
"""


def walk(matrix, path, visited, dim, exit, wall='W'):
    """
    Recursive function to walk a matrix path,
    avoiding to get out of index or to hit a wall ('W' symbol)

    NOTE: matrix is a squared matrix (dim x dim)
    """
    position = path[-1]
    # print(len(visited))
    if position == exit:
        return True

    visited.append(position)
    x, y = position
    strategies = {
        "bottom": (x + 1 < dim, (x + 1, y)),
        "top": (x - 1 > 0, (x - 1, y)),
        "left": (y - 1 > 0, (x, y - 1)),
        "right": (y + 1 < dim, (x, y + 1)),
    }

    for label, (check_boundaries, (j, k)) in strategies.items():
        # if x >= 0 and y >= 0 and x < dim and y < dim:
        if check_boundaries and (j, k) not in visited and matrix[j][k] != wall:
            if walk(matrix, path + [(j, k)], visited, dim, exit):
                return True
    return False


def path_finder(maze, start=(0, 0)):
    matrix = [row for row in maze.splitlines()]
    dim = len(matrix)
    exit = (dim - 1, dim - 1)
    return walk(matrix, [start], list(), dim, exit)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
