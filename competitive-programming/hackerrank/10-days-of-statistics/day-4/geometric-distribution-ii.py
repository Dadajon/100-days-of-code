def geometric_distribution(n, p):
    res = 0
    q = 1.0 - p
    for i in range(n + 1):
        if i > 0:
            res += q ** (i - 1) * p
    return res


if __name__ == "__main__":
    probability = list(map(int, input().split()))
    number_of_inspections = int(input())
    p = probability[0] / probability[1]

    # Get binomial result
    result = geometric_distribution(number_of_inspections, p)

    print(round(result, 3))