def forming_magic_square(s):
    """
    You will be given a 3 x 3 matrix s of integers in the inclusive range [1, 9].
    We can convert any digit a to any other digit b in the range [1, 9] at cost of |a - b|.
    Given s, convert it into a magic square at minimal cost.
    Print this cost on a new line.

    :param s: a 3 x 3 array of integers
    :return: an integer denoting the minimum cost of turning matrix s into a magic square.
    """
    all_squares = [
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
    ]
    min_cost = 9 * 9
    for magic_square in all_squares:
        cost = 0
        for i in range(3):
            for j in range(3):
                cost += abs(magic_square[i][j] - s[i][j])
        if cost < min_cost:
            min_cost = cost
    return min_cost


if __name__ == '__main__':
    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = forming_magic_square(s)

    print(str(result) + '\n')