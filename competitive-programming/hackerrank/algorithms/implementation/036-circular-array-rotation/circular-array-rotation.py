def circular_array_rotation(arr, rotations, queries):
    """
    One rotation operation moves the last array element to the first position and shifts all remaining elements right one.
    
    :param arr: an array of integers to rotate
    :param rotations: an integer, the rotation count
    :param queries: an array of integers, the indices to report
    :return: an array of integers representing the values at the specified indices
    """
    res = []

    for _ in range(rotations):
        tmp = arr[-1]
        arr.pop(-1)
        arr.insert(0, tmp)

    for i in queries:
        res.append(arr[i])

    return res


if __name__ == '__main__':
    n, k, q = map(int, input().rstrip().split())
    a = list(map(int, input().rstrip().split()))
    queries = []

    for _ in range(q):
        queries_item = int(input())
        queries.append(queries_item)

    result = circular_array_rotation(a, k, queries)

    print('\n'.join(map(str, result)))
    print('\n')
