import math


def standard_deviation(n, a):
    """
    Given an array, X, of N integers, calculate and print the standard deviation.
    Your answer should be in decimal form, rounded to a scale of 1 decimal place (i.e., 12.3 format).
    An error margin of ± 0.1 will be tolerated for the standard deviation.

    :param n: the number of elements in the array.
    :param a: input array
    :return: print standard deviation (STDEV)
    """
    mean = sum(a) / n
    sum_of_squared_elements = 0

    for i in range(n):
        sum_of_squared_elements += (a[i] - mean) ** 2

    variance = sum_of_squared_elements // n
    get_stdev = math.sqrt(variance)

    print("{0:.1f}".format(get_stdev))


if __name__ == '__main__':
    N = int(input())
    input_array = list(map(int, input().rstrip().split()))

    standard_deviation(N, input_array)