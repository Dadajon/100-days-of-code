#!/bin/python3


def multiplication(input_number):
    """
    Given an integer, n, print its first 10 multiples.
    Each multiple n*i (where 1 ≤ i ≤ 10) should be printed on a new line in the form: n * i = result.

    :param input_number: a single integer number ( 2 ≤ n ≤ 20).
    :return: Print 10 lines of output; each line i (where 1 ≤ i ≤ 10) contains the result of n*i in the form: n * i = result.
    """
    for i in range(1, 11):
        result = input_number * i
        print("{} x {} = {}".format(input_number, i, result))


if __name__ == '__main__':
    n = int(input())
    if n < 2 or n > 20:
        print("Out of range (2 ≤ n ≤ 20)")
    else:
        multiplication(n)