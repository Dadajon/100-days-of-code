def beautiful_days(start_day, end_day, divisor_k):
    days = [x for x in range(start_day, end_day + 1)]
    cnt = 0
    for day in days:
        if abs(day - int(str(day)[::-1])) % divisor_k == 0:
            cnt += 1

    return cnt


if __name__ == '__main__':
    i, j, k = map(int, input().rstrip().split())
    result = beautiful_days(i, j, k)
    print(str(result) + '\n')
