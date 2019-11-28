def save_the_prisoner(n, m, s):
    warn_seat = ((s - 1) + (m - 1)) % n + 1
    return warn_seat


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n, m, s = map(int, input().rstrip().split())
        result = save_the_prisoner(n, m, s)
        print(str(result) + '\n')
