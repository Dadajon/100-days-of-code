def factorial(n):
    if n == 1 or n == 0:
        return 1
    if n > 1:
        return factorial(n - 1) * n


def binomial(x, n, p):
    f = factorial(n) / (factorial(x) * factorial(n - x))
    return f * p ** x * (1.0 - p) ** (n - x)


if __name__ == "__main__":
    values = list(map(float, input().split()))
    p = values[0] / (values[0] + values[1])
    n = 6

    result = binomial(3, n, p) + binomial(4, n, p) + binomial(5, n, p) + binomial(6, n, p)
    print(round(result, 3))