
from math import *


def squares(lower_range, upper_range):
    """

    :param lower_range:
    :param upper_range:
    :return:
    """
    count = floor(sqrt(b)) - ceil(sqrt(a)) + 1
    return count


if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        ab = input().split()
        a = int(ab[0])
        b = int(ab[1])

        result = squares(a, b)
        print(str(result) + '\n')
