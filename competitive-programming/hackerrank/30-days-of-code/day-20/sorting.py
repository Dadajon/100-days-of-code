if __name__ == "__main__":
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))

    number_of_swaps = 0
    for i in range(n):
        current_swap = 0
        for j in range(n - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                current_swap += 1
                number_of_swaps += 1

        if current_swap == 0:
            break

    print("Array is sorted in {} swaps.".format(number_of_swaps))
    print("First Element: {}".format(a[0]))
    print("Last Element: {}".format(a[-1]))