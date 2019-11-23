def strange_grid(r, c):
    return (r - (r % 2 == 0)) // 2 * 10 + (r % 2 == 0) + (c - 1) * 2


if __name__ == '__main__':
    r, c = map(int, input().rstrip().split())

    result = strange_grid(r, c)
    print(str(result) + '\n')
