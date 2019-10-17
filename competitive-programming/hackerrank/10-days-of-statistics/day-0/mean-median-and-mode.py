from scipy import stats


def find_mean_median_mode(n, _array):
    """
    Print  lines of output in the following order:
        * Print the mean on a new line, to a scale of 1 decimal place (i.e., 12.3, 7.0).
        * Print the median on a new line, to a scale of 1 decimal place (i.e., 12.3, 7.0).
        * Print the mode on a new line; if more than one such value exists, print the numerically smallest one.

    :param n: the number of elements in the array
    :param _array: n space-separated integers describing the array's elements.
    :return: mean, median, mode
    """
    mean = sum(_array) / n

    sorted_array = sorted(_array)
    if len(sorted_array) % 2 == 0:
        median = (sorted_array[n // 2 - 1] + sorted_array[n // 2]) / 2
    else:
        median = sorted_array[n // 2]

    get_mode = stats.mode(_array)

    print(f"{mean}\n{median}\n{get_mode[0][0]}")


if __name__ == '__main__':
    N = int(input())

    array_items = input().rstrip().split()
    input_array = list(map(int, array_items))

find_mean_median_mode(N, input_array)