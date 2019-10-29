
def breakingRecords(scores):
    """
    Given Maria's scores for a season,
    find and print the number of times she breaks her records for most and least points scored during the season.
    :param scores: Maria's scores
    :return: an integer array containing the numbers of times she broke her records
    """
    maxi = scores[0]
    mini = scores[0]
    max_count = 0
    min_count = 0
    for i in range(len(scores)):
        if scores[i] > maxi:
            maxi = scores[i]
            max_count += 1
        if scores[i] < mini:
            mini = scores[i]
            min_count += 1
    return [max_count, min_count]


if __name__ == '__main__':
    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    print(' '.join(map(str, result)))
    print('\n')