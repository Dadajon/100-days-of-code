def interquartile_range(n, a_x, a_f):
    """
    The interquartile range of an array is the difference between its first (Q1) and third (Q3) quartiles (i.e., Q3 - Q1).
    Given an array, X, of N integers and an array, F, representing the respective frequencies of X's elements, construct a data set, S, where each x_i occurs at frequency f_i.
    Then calculate and print S's interquartile range, rounded to a scale of 1 decimal place (i.e., 12.3 format).

    :param n: the number of elements in arrays X and F.
    :param a_x: input array X
    :param a_f: input array Y
    :return: print the interquartile range for the expanded data set on a new line. Round your answer to a scale of 1 decimal place (i.e., 12.3 format).
    """
    S = list()
    left_a = list()
    right_a = list()
    temp = 1

    for i in range(n):
        for j in range(a_f[i]):
            S.append(a_x[i])

    sorted_s = sorted(S)

    for i in range(len(sorted_s) // 2):
        left_a.append(sorted_s[i])
        right_a.append(sorted_s[i - temp])
        temp += 2

    # Q1
    if len(left_a) % 2 == 0:
        quartile_1 = (left_a[len(left_a) // 2 - 1] + left_a[len(left_a) // 2]) // 2
    else:
        quartile_1 = left_a[len(left_a) // 2]

    # Q3
    if len(right_a) % 2 == 0:
        quartile_3 = (right_a[len(right_a) // 2 - 1] + right_a[len(right_a) // 2]) // 2
    else:
        quartile_3 = right_a[len(right_a) // 2]

    result = quartile_3 - quartile_1
    return result


if __name__ == "__main__":
    N = int(input())

    array_x = list(map(int, input().rstrip().split()))
    array_f = list(map(int, input().rstrip().split()))

    iqr = interquartile_range(N, array_x, array_f)

    print("{0:.1f}".format(iqr))