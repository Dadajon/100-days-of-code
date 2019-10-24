def review(st):
    st1 = ''
    st2 = ''
    for i in range(len(st)):
        if i % 2 == 0:
            st1 += st[i]
        else:
            st2 += st[i]
    print(st1 + " " + st2)


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        input_string = input()
        review(input_string)