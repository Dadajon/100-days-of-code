def even_fib_nums(N):
    A, B, C = 1, 2, 3
    evens_sum = 2
    while C < N:
        if not C % 2:
            print(not C % 2)
            print(C)
            evens_sum += C
        A, B, C = B, C, B + C
    return evens_sum


if __name__ == "__main__":
    t = int(input().strip())

    for _ in range(t):
        n = int(input().strip())
        result = even_fib_nums(n)
        print(result)
