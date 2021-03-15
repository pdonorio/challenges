"""
>>> snail([[1,2,3], [4,5,6], [7,8,9]])
[1, 2, 3, 6, 9, 8, 7, 4, 5]

>>> snail([[1,2,3], [8,9,4], [7,6,5]])
[1, 2, 3, 4, 5, 6, 7, 8, 9]
"""
from itertools import chain


directions = {
    "right": (
        lambda vectors, x, y: len(vectors[x]) > y + 1,
        lambda x, y: (x, y + 1),
    ),
    "down": (
        lambda vectors, x, y: len(vectors) > x + 1,
        lambda x, y: (x + 1, y),
    ),
    "left": (
        lambda vectors, x, y: y > 0,
        lambda x, y: (x, y - 1),
    ),
    "up": (
        lambda vectors, x, y: x > 0,
        lambda x, y: (x - 1, y),
    ),
}


def snail(vectors):
    x = 0
    y = 0
    path = []
    if sum(map(len, vectors)) < 1:
        return path

    possible_directions = iter(list(directions.keys()) * len(vectors))
    current_direction = next(possible_directions)
    verify, move = directions[current_direction]

    while set(map(len, vectors)).pop() > 0:

        # visit current position
        path.append(vectors[x][y])
        vectors[x][y] = -1
        # print(vectors, x, y, current_direction, path)

        # if all positions have been visited
        if set(chain(*vectors)) == {-1}:
            break

        # make next move
        change = False
        while True:
            if verify(vectors, x, y):
                j, k = move(x, y)
                next_value = vectors[j][k]
                # print("moving", x, y, j, k, next_value)
                if next_value >= 0:
                    break
                else:
                    change = True
            else:
                change = True

            if change:
                # print("change")
                current_direction = next(possible_directions)
                verify, move = directions[current_direction]
            # time.sleep(1)
        x, y = j, k

    return path


if __name__ == '__main__':
    # snail([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    import doctest

    doctest.testmod()
