def get_hourglass_sum(array_2d, row, col):
    up_left = array_2d[row - 1][col - 1]
    up = array_2d[row - 1][col]
    up_right = array_2d[row - 1][col + 1]
    current = array_2d[row][col]
    down_left = array_2d[row + 1][col - 1]
    down = array_2d[row + 1][col]
    down_right = array_2d[row + 1][col + 1]
    hourglass_sum = up_left + up + up_right + current + down_left + down + down_right
    return hourglass_sum


def calculate_hourglasses(array_2d):
    """
    Calculate the hourglass sum for every hourglass in A, then print the maximum hourglass sum.
    :param array_2d: 6 space-separated integers describing 2D Array A; every value in A will be in the inclusive range of -9 to 9.
    :return: the maximum hourglass sum
    """
    # -9 ≤ A[i][j] ≤ 9 => -9 * 6 - 1 = -63
    max_hourglass_sum = -63
    for i in range(1, len(array_2d) - 1):
        for j in range(1, len(array_2d) - 1):
            current_hourglass_sum = get_hourglass_sum(array_2d, i, j)

            if current_hourglass_sum > max_hourglass_sum:
                max_hourglass_sum = current_hourglass_sum

    return max_hourglass_sum


if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = calculate_hourglasses(arr)
    print(result)