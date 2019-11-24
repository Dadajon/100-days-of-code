def climbing_leaderboard(leaderboard, alice_scores):
    rankings = createRankings(leaderboard)
    i = len(leaderboard) - 1
    for score in alice_scores:
        flag = True
        while flag:
            if i == -1:
                print(1)
                flag = False
            elif score < leaderboard[i]:
                print(rankings[i] + 1)
                flag = False
            elif score == leaderboard[i]:
                print(rankings[i])
                flag = False
            elif score > leaderboard[i]:
                i -= 1
    return


def createRankings(leaderboard):
    rankings = [1]
    rank = 1
    for i in range(1, len(leaderboard)):
        if leaderboard[i] < leaderboard[i - 1]:
            rank += 1
        rankings.append(rank)
    return rankings


if __name__ == "__main__":
    scores_count = int(input())
    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())
    alice = list(map(int, input().rstrip().split()))

    climbing_leaderboard(scores, alice)
