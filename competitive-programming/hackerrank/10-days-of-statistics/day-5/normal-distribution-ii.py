
import math


def cumulative_distribution(mu, sigma, x):
    """
    The final grades for a Physics exam taken by a large group of students have a mean of 70 and a standard deviation of 10.
    If we can approximate the distribution of these grades by a normal distribution, what percentage of the students:
        1. Scored higher than 80 (i.e., have a grade > 80)?
        2. Passed the test (i.e., have a grade grade ≥ 60)?
        3. Failed the test (i.e., have a grade < 60)?

    Find and print the answer to each question on a new line, rounded to a scale of 2 decimal places.

    :param mu: mean
    :param sigma: standard deviation
    :param x: input value
    :return: cumulative distribution
    """
    return 0.5 * (1 + math.erf((x - mu) / (sigma * (2 ** 0.5))))


if __name__ == "__main__":
    mu_and_sigma = list(map(int, input().rstrip().split()))
    a = int(input())
    b = int(input())

    mu = mu_and_sigma[0]
    sigma = mu_and_sigma[1]

    print(round(100 - (cumulative_distribution(mu, sigma, a) * 100), 2))
    print(round(100 - (cumulative_distribution(mu, sigma, b) * 100), 2))
    print(round(cumulative_distribution(mu, sigma, b) * 100, 2))

