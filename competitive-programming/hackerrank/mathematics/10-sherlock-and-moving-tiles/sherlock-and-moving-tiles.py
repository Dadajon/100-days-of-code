import math


def movingTiles(l, s1, s2, queries):
    for i in queries:
        rep = math.sqrt(2) * (l - math.sqrt(i)) / abs(s2 - s1)
        print("{0:.20f}".format(rep))


if __name__ == '__main__':
    l_s1_s2 = input().split()

    l = int(l_s1_s2[0])
    s1 = int(l_s1_s2[1])
    s2 = int(l_s1_s2[2])

    queries_count = int(input())

    queries = []
    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    movingTiles(l, s1, s2, queries)
