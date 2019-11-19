def sum_digits(num):
    r = 0
    while num:
        r, num = r + num % 10, num // 10
    return r


if __name__ == '__main__':
    n = int(input())
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)

    print(max(divisors, key=sum_digits))
