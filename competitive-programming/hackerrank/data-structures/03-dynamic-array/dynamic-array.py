#!/bin/python3

def dynamicArray(n, queries):
    """
    Create a list, seqList, of N empty sequences, where each sequence is indexed from 0 to N-1.
    The elements within each of the N sequences also use 0-indexing.
    Create an integer, lastAns, and initialize it to 0.
    The types of queries that can be performed on your list of sequences (seqList) are described below:

    1] Query: 1 . y
        1] Find the sequence, seq, at index ((x xor lastAns) % N) in seqList.
        2] Append integer y to sequence seq
    2] Query: 2 . y
        1] Find the sequence, seq, at index ((x xor lastAns) % N) in seqList.
        2] Find the value of element y % size in seq (where size is the size of seq) and assign it to lastAns.
        3] Print the new value of lastAns on a new line

    :param n: 2
    :param queries: length = 5,  [[1, 0, 5], [1, 1, 7], [1, 0, 3], [2, 1, 0], [2, 1, 1]]
    :return:
    """

    last_ans = 0
    seq_list = [[] for _ in range(n)]  # [[], []]
    result = []

    for i in queries:
        # for j in queries[i]:
        q, x, y = i[0], i[1], i[2]

        index = (x ^ last_ans) % n
        seq = seq_list[index]
        if q == 1:
            seq.append(y)
            # print(seq)
        elif q == 2:
            size = len(seq)
            last_ans = seq[y % size]
            # print(last_ans)
            result.append(last_ans)
    return result

first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
q = int(first_multiple_input[1])
queries = []

for _ in range(q):
    queries.append(list(map(int, input().rstrip().split())))

result = dynamicArray(n, queries)
print('\n'.join(map(str, result)))
