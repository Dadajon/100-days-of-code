import math

if __name__ == "__main__":
    value = float(input())
    mean = float(input())
    stdev = float(input())
    mid = float(input())
    z = float(input())

    ci_value = z * (stdev / math.sqrt(value))

    print(round(mean - ci_value, 2))
    print(round(mean + ci_value, 2))