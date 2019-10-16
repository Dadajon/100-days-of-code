def matchingStrings(strings, queries):
    """
    Complete the function matchingStrings in the editor below.
    The function must return an array of integers representing the frequency of occurrence of each query string in strings.

    :param strings: an array of strings to search
    :param queries: an array of query strings
    :return: an integer array of the results of all queries in order.
    """
    result = []

    for i in queries:
        result.append(strings.count(i))

    return result


if __name__ == '__main__':
    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    print('\n'.join(map(str, res)))