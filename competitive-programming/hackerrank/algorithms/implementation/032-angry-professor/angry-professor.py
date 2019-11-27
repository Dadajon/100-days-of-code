def angry_professor(threshold, arrival_times):
    punctual_students = [x for x in arrival_times if x <= 0]
    if len(punctual_students) >= threshold:
        return "NO"
    else:
        return "YES"


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n, k = map(int, input().rstrip().split())
        a = list(map(int, input().rstrip().split()))

        result = angry_professor(k, a)

        print(result + '\n')
