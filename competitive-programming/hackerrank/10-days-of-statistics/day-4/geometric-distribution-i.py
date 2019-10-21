def geometric_distribution(n, p):
    return (1.0-p) ** (n - 1) * p


if __name__ == "__main__":
    probability = list(map(int, input().split()))
    number_of_inspections = int(input())
    p = probability[0] / probability[1]

    # Get binomial result
    result = geometric_distribution(number_of_inspections, p)

    print(round(result, 3))
