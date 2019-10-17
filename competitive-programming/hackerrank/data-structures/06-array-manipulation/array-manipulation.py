
def array_manipulation(elem_num, input_queries):
    """
    Complete the function arrayManipulation in the editor below. It must return an integer, the maximum value in the resulting array.

    :param elem_num: the number of elements in your array
    :param input_queries: a two dimensional array of queries where each queries[i] contains three integers, a, b, and k.
    :return: the integer maximum value in the finished array.
    """
    zeros = [0 for _ in range(elem_num + 1)]

    for i in input_queries:
        a, b, k = i[0], i[1], i[2]
        zeros[a - 1] += k
        zeros[b] -= k

    get_max = 0
    _sum = 0

    for i in zeros:
        _sum += i
        if _sum > get_max:
            get_max = _sum

    return get_max


if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = array_manipulation(n, queries)

    print(str(result) + '\n')
