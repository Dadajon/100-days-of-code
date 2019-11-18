def hurdle_race(k, height):
    """
    Dan is playing a video game in which his character competes in a hurdle race.
    Hurdles are of varying heights, and Dan has a maximum height he can jump.
    There is a magic potion he can take that will increase his maximum height by 1 unit for each dose.
    How many doses of the potion must he take to be able to jump all of the hurdles.

    :param k: an integer denoting the height Dan can jump naturally
    :param height: an array of integers denoting the heights of each hurdle
    :return: the minimum units of potion Dan needs to drink to jump all of the hurdles
    """
    if k < max(height):
        return max(height) - k
    else:
        return 0


if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])

    height = list(map(int, input().rstrip().split()))
    result = hurdle_race(k, height)

    print(str(result) + '\n')