def restaurant(length, breadth):
    """
    Martha is interviewing at Subway. One of the rounds of the interview requires her to cut
    a bread of size lxb into smaller identical pieces such that each piece is a square having
    maximum possible side length with no left over piece of bread.

    :param length: the length of the bread
    :param breadth: the breadth of the bread
    :return: T lines, each containing an integer that denotes the number of squares of maximum size,
             when the bread is cut as per the given condition.
    """
    greatest_common_divisor = 1
    min_input = min(length, breadth)

    if length == breadth:
        return 1
    else:
        for i in range(1, min_input + 1):
            if length % i == 0 and breadth % i == 0:
                print(i)
                greatest_common_divisor = i

    return (length * breadth) // (greatest_common_divisor ** 2)


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        lb = input().split()

        l = int(lb[0])
        b = int(lb[1])
        result = restaurant(l, b)

        print(str(result) + '\n')
