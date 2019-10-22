import math


def cumulative_distribution(w, mu, sigma):
    return 0.5 * (1 + math.erf((w - mu) / (sigma * (2 ** 0.5))))


if __name__ == "__main__":
    max_weight = float(input())
    cargo_size = float(input())
    mean = float(input())
    stdev = float(input())

    new_mean = cargo_size * mean
    new_stdev = math.sqrt(cargo_size) * stdev

    dist = cumulative_distribution(max_weight, new_mean, new_stdev)
    print(round(dist, 4))
