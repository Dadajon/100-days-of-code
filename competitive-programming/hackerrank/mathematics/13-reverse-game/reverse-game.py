def find_result(n, k):
    if k == n / 2:
        return n
    elif k < n / 2:
        return (k + 1) * 2 - 1
    else:
        return (n - k) * 2


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n, k = map(int, input().rstrip().split())
        print(find_result(n - 1, k))
