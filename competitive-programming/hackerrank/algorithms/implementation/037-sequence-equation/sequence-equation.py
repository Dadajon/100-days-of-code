
def permutation_equation(permute_arr):
    """

    :param permute_arr: an array of integers
    :return: an array of integers that represent the values of y
    """

    return [(p.index(p.index(i) + 1) + 1) for i in range(1, max(p) + 1)]


if __name__ == '__main__':
    n = int(input())
    p = list(map(int, input().rstrip().split()))

    result = permutation_equation(p)

    print('\n'.join(map(str, result)))
    print('\n')
