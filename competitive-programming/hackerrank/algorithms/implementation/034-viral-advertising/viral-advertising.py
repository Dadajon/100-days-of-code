def viral_advertising(n):
    shared = 5
    linked = shared // 2
    cumulative = 0

    for _ in range(n):
        cumulative += linked
        shared = linked * 3
        linked = shared // 2

    return cumulative


if __name__ == '__main__':
    n = int(input())

    result = viral_advertising(n)

    print(str(result) + '\n')
