if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    for items in arr[::-1]:
        print(items, end=" ")