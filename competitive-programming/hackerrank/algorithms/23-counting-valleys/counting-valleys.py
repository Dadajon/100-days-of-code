def counting_valleys(n_steps, path):
    """
    Given Gary's sequence of up and down steps during his last hike, find and print the number of valleys he walked through.
    :param n_steps: the number of steps Gary takes
    :param path: a string describing his path
    :return: an integer that denotes the number of valleys Gary traversed
    """
    level, num_valleys = 0, 0
    for i in range(n_steps):
        if path[i] == 'U':
            level += 1
            if level == 0:
                num_valleys += 1
        else:
            level -= 1
    return num_valleys


if __name__ == '__main__':
    n = int(input())

    s = input()

    result = counting_valleys(n, s)

    print(str(result) + '\n')