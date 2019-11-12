def find_max_bitwise(N, K):
    max_bitwise = 0
    for i in range(1, N + 1):
        for j in range(1, i):
            bitwise = i & j
            if max_bitwise < bitwise < K:
                max_bitwise = bitwise
                if max_bitwise == k - 1:
                    return max_bitwise

    return max_bitwise


if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        nk = input().split()

        n = int(nk[0])
        k = int(nk[1])

        print(find_max_bitwise(n, k))