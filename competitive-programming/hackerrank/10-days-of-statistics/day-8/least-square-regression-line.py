import statistics as st

if __name__ == "__main__":
    n = 5
    x = []
    y = []

    for i in range(5):
        xl_el, y_el = list(map(int, input().rstrip().split()))
        x.append(xl_el)
        y.append(y_el)

    mean_x = st.mean(x)
    mean_y = st.mean(y)

    x_squared = sum([x[i] ** 2 for i in range(n)])
    xy = sum([x[i] * y[i] for i in range(n)])

    b = (n * xy - sum(x) * sum(y)) / (n * x_squared - (sum(x) ** 2))
    a = mean_y - b * mean_x

    print(round(a + 80 * b, 3))