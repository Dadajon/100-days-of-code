def quartiles(n, a):
    """
    Given an array, X, of N integers, calculate the respective first quartile (Q1), second quartile (Q2), and third quartile (Q3).
    It is guaranteed that Q1, Q2, and Q3 are integers.

    :param n: the number of elements in the array.
    :param a: input array
    :return: Print  lines of output in the following order:
                1. The first line should be the value of Q1.
                2. The second line should be the value of Q2.
                3. The third line should be the value of Q3.
    """
    sorted_a = sorted(a)
    left_a = list()
    right_a = list()
    temp = 1

    for i in range(n // 2):
        left_a.append(sorted_a[i])
        right_a.append(sorted_a[i - temp])
        temp += 2

    # Q2
    if n % 2 == 0:
        quartile_2 = (sorted_a[n // 2 - 1] + sorted_a[n // 2]) // 2
    else:
        quartile_2 = sorted_a[n // 2]

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

    print(quartile_1)
    print(quartile_2)
    print(quartile_3)


if __name__ == '__main__':
    N = int(input())
    input_array = list(map(int, input().rstrip().split()))

    quartiles(N, input_array)
