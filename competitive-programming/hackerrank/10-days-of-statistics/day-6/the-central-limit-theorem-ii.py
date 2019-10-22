import math


def cumulative_distribution(t, mu, sigma):
    return 0.5 * (1 + math.erf((t - mu) / (sigma * (2 ** 0.5))))


if __name__ == "__main__":
    tickets_left = float(input())
    eager_students = float(input())
    mean = float(input())
    stdev = float(input())

    new_mean = eager_students * mean
    new_stdev = math.sqrt(eager_students) * stdev

    dist = cumulative_distribution(tickets_left, new_mean, new_stdev)
    print(round(dist, 4))