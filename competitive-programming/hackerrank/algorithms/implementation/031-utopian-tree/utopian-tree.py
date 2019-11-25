def utopian_tree(n_cycles):
    """
    The Utopian Tree goes through 2 cycles of growth every year. Each spring, it doubles in height. Each summer, its height increases by 1 meter.

    Laura plants a Utopian Tree sapling with a height of 1 meter at the onset of spring. How tall will her tree be after n growth cycles?

    :param n_cycles: an integer, the number of growth cycles to simulate
    :return: the height of the Utopian Tree after n cycles
    """
    height_tree = 1

    if n_cycles == 0:
        return height_tree

    for i in range(1, n_cycles + 1):
        if i % 2 == 0:
            height_tree += 1
        else:
            height_tree *= 2

    return height_tree


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())
        result = utopian_tree(n)
        print(str(result) + '\n')
