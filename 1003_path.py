def dfs(matrix: list, end: tuple, path: list, visited: list):
    """
    idea was scratched from
    https://www.educative.io/edpresso/how-to-implement-depth-first-search-in-python
    """

    current = path[-1]
    if current == end:
        print(f"Path: {path}")
        return True

    if current not in visited:
        # print("current", current)
        visited.append(current)
        x, y = current
        strategies = {
            (x, y + 1): y < len(matrix) - 1,
            (x, y - 1): y > 0,
            (x + 1, y): x < len(matrix) - 1,
            (x - 1, y): x > 0,
        }
        for nb, condition in strategies.items():
            # print(nb, condition)
            # if condition:
            #     print(matrix[nb[0]][nb[1]])
            if condition and matrix[nb[0]][nb[1]]:
                if dfs(matrix, end, path + [nb], visited):
                    return True
    return False


if __name__ == '__main__':

    matrix = [
        [1, 1, 0, 1, 0],
        [0, 1, 0, 1, 1],
        [1, 1, 1, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 1],
    ]

    tests = [
        ((0, 0), (3, 3)),
        ((0, 1), (0, 4)),
        ((1, 4), (2, 0)),
    ]

    for points in tests:
        print("Points", points)
        print(dfs(matrix, end=points[1], path=[points[0]], visited=[]))
        print()
