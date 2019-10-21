def factorial(num):
    if num == 0 or num == 1:
        return 1
    if num > 1:
        return factorial(num - 1) * num


def poisson_distribution(_lambda, k):
    e = 2.71828
    return (_lambda ** k * e ** (-_lambda)) / factorial(k)


if __name__ == "__main__":
    avg = float(input())
    actual_num_of_success = int(input())

    # Get binomial result
    result = poisson_distribution(avg, actual_num_of_success)

    print(round(result, 3))
