
import statistics as st


def pearson_correlation_coefficient(n, x, y):
    """
    Given two n-element data sets, X and Y, calculate the value of the Pearson correlation coefficient.

    :param n: an integer, n, denoting the size of data sets X and Y
    :param x: data set X
    :param y: data set Y
    :return: print the value of the Pearson correlation coefficient, rounded to a scale of 3 decimal places
    """
    pcc = 0
    mean_x = st.mean(x)
    stdev_x = st.pstdev(x)
    mean_y = st.mean(y)
    stdev_y = st.pstdev(y)

    for i in range(n):
        pcc += (x[i] - mean_x) * (y[i] - mean_y)
    return pcc / (n * stdev_x * stdev_y)


if __name__ == "__main__":
    n = int(input())
    X = list(map(float, input().rstrip().split()))
    Y = list(map(float, input().rstrip().split()))
    result = pearson_correlation_coefficient(n, X, Y)
    print(round(result, 3))