def extra_long_factorials(in_num):
    """
    Calculate and print the factorial of a given integer.
    Works well up to in_num = 998, than "RecursionError: maximum recursion depth exceeded in comparison" occurred

    :param in_num: an integer
    :return: factorial of in_num
    """
    if n == 1 or n == 0:
        return 1
    if n > 1:
        return extra_long_factorials(n - 1) * n


if __name__ == '__main__':
    n = int(input())

    result = extra_long_factorials(n)

    print(result)
