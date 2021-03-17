"""
>>> path_finder("\\n".join([]))
False
>>> path_finder("\\n".join([ ".W.", ".W.", "..." ]))
True
>>> path_finder("\\n".join([ ".W.", ".W.", "W.." ]))
False
>>> path_finder("\\n".join([ "......", "......", "......", "......", "......", "......" ]))
True
>>> path_finder("\\n".join([ "......", "......", "......", "......", ".....W", "....W." ]))
False
"""

DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def path_finder(maze, start=(0, 0)):
    matrix = [list(line) for line in maze.splitlines()]
    # print(matrix)
    Q = [start]
    N = len(matrix)

    while Q:
        # print(Q)
        x, y = Q.pop()
        if x == N - 1 and y == N - 1:
            return True
        if x >= 0 and y >= 0 and x < N and y < N:
            if matrix[x][y] == '.':
                matrix[x][y] = 'X'
                # print(matrix)
                for j, k in DIRECTIONS:
                    Q.append([x + j, y + k])
    return False


if __name__ == '__main__':
    import doctest

    doctest.testmod()
