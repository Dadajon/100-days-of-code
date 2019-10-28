
def connectingTowns(n, routes):
    paths = 1
    for i in routes:
        paths = (paths * i) % 1234567
    return paths


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        routes = list(map(int, input().rstrip().split()))

        result = connectingTowns(n, routes)

        print(str(result) + '\n')
