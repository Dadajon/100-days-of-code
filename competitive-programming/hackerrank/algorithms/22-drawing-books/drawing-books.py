def page_count(num_page, goal_p):
    """
    Return the minimum number of pages Brie must turn.
    :param num_page: the number of pages in the book
    :param goal_p: the page number to turn to
    :return: an integer denoting the minimum number of pages Brie must turn to get to page p.
    """
    last_page = num_page // 2
    goal_page = goal_p // 2
    return min(goal_page, last_page - goal_page)


if __name__ == '__main__':
    n = int(input())

    p = int(input())

    result = page_count(n, p)

    print(str(result) + '\n')