def get_rank(d):
    """
    Get Rank
    :param d: dataset
    :return: rank
    """
    rank = dict()
    sort = sorted(d)
    for i in range(len(d)):
        for j in range(len(sort)):
            if d[i] == sort[j]:
                rank[d[i]] = j + 1
    return rank


def get_spearman(x, y, rx, ry, n):
    """
    Given two N-element data sets, X and Y, calculate the value of Spearman's rank correlation coefficient.

    :param x: dataset X
    :param y: dataset Y
    :param rx: rank of X
    :param ry: rank of Y
    :param n: an integer, N, denoting the number of values in data sets X and Y.
    :return: the value of the Spearman's rank correlation coefficient, rounded to a scale of 3 decimal places.
    """
    diff_rank = 0
    for i in range(n):
        if rx[x[i]] != ry[y[i]]:
            diff_rank = diff_rank + ((rx[x[i]] - ry[y[i]]) ** 2)
    return (6 * diff_rank) / (n ** 3 - n)


if __name__ == "__main__":
    n = int(float(input()))
    x = list(map(float, input().split()))
    y = list(map(float, input().split()))

    rank_x = get_rank(x)
    rank_y = get_rank(y)

    s = get_spearman(x, y, rank_x, rank_y, n)
    print(round(1 - s, 3))
