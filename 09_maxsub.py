def max_sequence(arr: list) -> int:
    positions = len(arr) + 1
    sums = [sum(arr[j:k]) for j in range(positions) for k in range(j + 1, positions)]
    return max(max(sums, default=0), 0)

    # return max([sum(arr[i:j]) for i in range(len(arr)+1) for j in range(len(arr)+1)])


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_sequence(nums))
