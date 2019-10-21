
import math


def cumulative_distribution(mu, sigma, x):
    """
    In a certain plant, the time taken to assemble a car is a random variable, X,
    having a normal distribution with a mean of 20 hours and a standard deviation of 2 hours.
    What is the probability that a car can be assembled at this plant in:
        1. Less than 19.5 hours?
        2. Between 20 and 22 hours?

    :param mu: mean
    :param sigma: standard deviation
    :param x: input value
    :return: cumulative distribution
    """
    return 0.5 * (1 + math.erf((x - mu) / (sigma * (2 ** 0.5))))


if __name__ == "__main__":
    mu_and_sigma = list(map(int, input().rstrip().split()))
    less_than = float(input())
    between_a_b = list(map(int, input().rstrip().split()))

    mu = mu_and_sigma[0]
    sigma = mu_and_sigma[1]
    a = between_a_b[0]
    b = between_a_b[1]

    print(round(cumulative_distribution(mu, sigma, less_than), 3))
    print(round(cumulative_distribution(mu, sigma, b) - cumulative_distribution(mu, sigma, a), 3))