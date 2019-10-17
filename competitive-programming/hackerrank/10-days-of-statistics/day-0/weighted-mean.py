def find_weighted_mean(n, s, w):
    """
    Given an array, X, of N integers and an array, W, representing the respective weights of X's elements, calculate and print the weighted mean of X's elements.
    Your answer should be rounded to a scale of 1 decimal place (i.e.,  12.3 format).

    :param n: the number of elements in arrays X and W.
    :param s: N space-separated integers describing the respective elements of array X.
    :param w: N space-separated integers describing the respective elements of array W.
    :return: the weighted mean.
    """
    s_plus_w = 0

    for i in range(n):
        s_plus_w += s[i] * w[i]

    weighted_mean = s_plus_w / sum(w)

    return weighted_mean


if __name__ == "__main__":
    N = int(input())

    scores = list(map(int, input().rstrip().split()))
    weights = list(map(int, input().rstrip().split()))

    result = find_weighted_mean(N, scores, weights)

    print(f"{result:.1f}")
