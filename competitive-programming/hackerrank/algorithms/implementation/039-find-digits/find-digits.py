def find_digits(n):
    """
    The function should return an integer representing the number of digits of d that are divisors of d.
    :param n: an integer to analyze
    :return: for every test case, count the number of digits in n that are divisors of n
    """
    cnt = 0
    tmp = n
    while tmp > 0:
        digit = tmp % 10
        if digit != 0 and n % digit == 0:
            cnt += 1
        tmp //= 10

    return cnt


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = find_digits(n)

        print(str(result) + '\n')
