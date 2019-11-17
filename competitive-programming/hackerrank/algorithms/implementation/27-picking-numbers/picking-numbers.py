def picking_numbers(arr):
    """
    Given an array of integers, find and print the maximum number of integers you can select from the
    array such that the absolute difference between any two of the chosen integers is less than or equal to 1.

    :param arr: an array of integers
    :return: an integer that represents the length of the longest array that can be created
    """
    multiset_max_len = 0
    multiset = []
    for i in range(len(a)):
        if i not in multiset:
            max_cnt = max((arr.count(arr[i]) + arr.count(a[i] + 1)), (arr.count(arr[i]) + arr.count(a[i] - 1)))
            if max_cnt > multiset_max_len:
                multiset_max_len = max_cnt
            multiset.append(i)
    return multiset_max_len


if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    result = picking_numbers(a)
    print(str(result) + '\n')