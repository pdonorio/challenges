def check_zero_on_position(matrix: list, x: int, y: int) -> bool:
    try:
        return matrix[x][y] == 0
    except IndexError:
        return False


def find_zeros_nb(matrix: list, point: tuple) -> list:
    # Return a list of the neighboring coordinates that are 0's
    x, y = point
    neighbors = {
        'top': lambda x, y: (x - 1, y),
        'top-left': lambda x, y: (x - 1, y - 1),
        'top-right': lambda x, y: (x - 1, y + 1),
        'right': lambda x, y: (x, y + 1),
        'bottom': lambda x, y: (x + 1, y),
        'bottom-left': lambda x, y: (x + 1, y - 1),
        'bottom-right': lambda x, y: (x + 1, y + 1),
        'left': lambda x, y: (x, y - 1),
    }

    nb = []
    for label, func in neighbors.items():
        j, k = func(x, y)
        if check_zero_on_position(matrix, j, k):
            nb.append((x, y))
    return nb


if __name__ == '__main__':
    matrix = [
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 0],
        [1, 0, 0, 0, 1],
        [1, 1, 0, 1, 1],
    ]
    tests = [
        (1, 1),
        (2, 2),
        (3, 2),
        (0, 0),
        (4, 0),
    ]

    for point in tests:
        print(point, "->", find_zeros_nb(matrix, point))
