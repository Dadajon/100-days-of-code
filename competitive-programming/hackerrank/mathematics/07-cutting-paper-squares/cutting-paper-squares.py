#!/bin/python3

def solve(n, m):
    """
    print a long integer denoting the minimum number of cuts needed to cut the entire paper into 1x1 squares.

    :param n: width of paper
    :param m: height of paper
    :return: number of cuts
    """
    return (n * m) // 1 - 1


if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    result = solve(n, m)

    print(str(result) + '\n')