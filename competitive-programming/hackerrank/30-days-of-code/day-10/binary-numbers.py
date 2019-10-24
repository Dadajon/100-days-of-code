if __name__ == "__main__":
    current_1s = cnt_consecutive_1s = 0

    n = int(input())
    res = bin(n).replace('0b', '')

    for i in range(len(res)):
        if res[i] == '1':
            current_1s += 1
            if current_1s > cnt_consecutive_1s:
                cnt_consecutive_1s = current_1s
        else:
            current_1s = 0

    print(cnt_consecutive_1s)