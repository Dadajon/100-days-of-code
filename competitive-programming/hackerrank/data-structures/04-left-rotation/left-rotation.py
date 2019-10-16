#!/bin/python3

def left_rotate(_n, _d, _a):
    """

    Given an array of n integers and a number, d, perform d left rotations on the array.
    Then print the updated array as a single line of space-separated integers.

    :param _n: the number of integers
    :param _d: the number of left rotations you must perform
    :param _a: input array of n integers
    :return: print the updated array as a single line of space-separated integers.
    """
    for _ in range(_d):
        print(_a)
        temp = _a.pop(0)
        print(temp)
        print(_a)
        _a.append(temp)

    for i in _a:
        print(i, end=" ")

if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    left_rotate(n, d, a)
