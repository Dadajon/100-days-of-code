def factorial(n):
    if n == 1 or n == 0:
        return 1
    if n > 1:
        return factorial(n - 1) * n


def binomial(x, n, p):
    f = factorial(n) / (factorial(x) * factorial(n - x))
    return f * p ** x * (1.0 - p) ** (n - x)


if __name__ == "__main__":
    values = list(map(int, input().split()))
    p = values[0]/100
    n = values[1]

    # Get binomial result
    result1 = 0
    result2 = 0
    for i in range(n + 2):
        if i < 3:
            result1 += binomial(i, n, p)
        else:
            result2 += binomial(i-1, n, p)

    print(round(result1, 3))
    print(round(result2, 3))