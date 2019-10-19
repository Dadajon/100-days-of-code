
def getTotalX(a, b):
    """

    :param a:
    :param b:
    :return:
    """
    return (sum([all(i % x == 0 for x in a) and all(x % i == 0 for x in b) for i in range(max(a), min(b) + 1)]))

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    print(str(total) + '\n')
