#!/bin/python3


def kangaroo(x1, v1, x2, v2):
    """
    Complete the function kangaroo.

    :param x1: starting position for kangaroo 1
    :param v1: jump distance for kangaroo 1
    :param x2: starting position for kangaroo 2
    :param v2: jump distance for kangaroo 2
    :return: return YES if they reach the same position at the same time, or NO if they don't.
    """

    if x2 > x1 and v2 > v1:
        return "NO"
    else:
        for n in range(10000):
            if (x1 + v1) == (x2 + v2):
                return "YES"
            x1 += v1
            x2 += v2
        return "NO"


if __name__ == '__main__':
    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    print(result + '\n')
