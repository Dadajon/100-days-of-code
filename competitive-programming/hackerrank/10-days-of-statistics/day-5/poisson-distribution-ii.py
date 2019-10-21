if __name__ == "__main__":
    avg = list(map(float, input().rsplit()))
    result1 = 160 + 40*(avg[0]+avg[0]**2)
    result2 = 128 + 40 * (avg[1] + avg[1] ** 2)

    print(round(result1, 3))
    print(round(result2, 3))