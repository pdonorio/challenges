"""
- OA: Given a 2d matrix with chars and a target string. Check if the matrix contains this target string by only going right or down each time from the beginning point.
"""


def check_position(grid, word, i, j, pos=0):
    """
    O(n*2) = O(n)
    """
    if pos >= len(word) or i >= len(grid) or j >= len(grid):
        return False

    char = word[pos]
    # print("check", pos, char, i, j)
    if grid[i][j] == char:
        if pos == len(word) - 1:
            return True
        # move down or right
        return check_position(grid, word, i + 1, j, pos + 1) or check_position(
            grid, word, i, j + 1, pos + 1
        )
    return False


def search_word(grid: list, word: str) -> bool:
    """
    O(n*n) = O(n^2)
    total = O(n^2 * n) = O(n^3)
    """
    print(f"Search: {word}")
    size = len(grid)

    for i in range(0, size):
        for j in range(0, size):
            # print(i, j, grid[i][j])
            if check_position(grid, word, i, j):
                return True
            # break

    return False


grid = ["axmy", "bgdf", "xeet", "raks"]
print(search_word(grid, "geeks"))
print(search_word(grid, "geeksz"))
