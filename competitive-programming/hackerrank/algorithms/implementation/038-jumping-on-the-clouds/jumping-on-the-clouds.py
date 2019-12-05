def jumping_on_clouds(cloud_types, jump_length):
    """
    The function should return an integer representing the energy level remaining after the game.

    :param cloud_types: an array of integers representing cloud types
    :param jump_length: an integer representing the length of one jump
    :return: the final energy level remaining after the game
    """
    energy = 100
    position = 0

    while True:
        position = (position + jump_length) % len(cloud_types)
        if cloud_types[position] == 1:
            energy -= 2
        energy -= 1

        if position == 0:
            break

    return energy


if __name__ == '__main__':
    n, k = map(int, input().rstrip().split())

    c = list(map(int, input().rstrip().split()))

    result = jumping_on_clouds(c, k)

    print(str(result) + '\n')
