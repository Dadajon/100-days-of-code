def summingSeries(n):
    """
    For each test case, print the required answer in a line.

    :param n: a single integer
    :return: answer % modulo
    """
    modulo = 1000000007
    answer = n * n % modulo

    return answer


if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = summingSeries(n)

        print(str(result) + '\n')