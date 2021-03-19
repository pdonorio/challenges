"""
Find all top-left corners of squares in binary 2D matrix.
Except for the last row and the last column, every single cell will be a top left corner of a square
"""


def find_corners(matrix: list) -> list:
    return [
        matrix[j][k] for j in range(len(matrix) - 1) for k in range(len(matrix[j]) - 1)
    ]


if __name__ == '__main__':
    matrix = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
    ]
    print(find_corners(matrix))
