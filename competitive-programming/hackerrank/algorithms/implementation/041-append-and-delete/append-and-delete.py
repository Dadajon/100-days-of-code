def append_and_delete(s, t, k):
    """

    Args:
        s: the initial string
        t: the desired string
        k: the number of operations

    Returns:
        Print Yes if function can obtain string t by performing exactly k operations on s. Otherwise, print No.
    """
    count_similar_char = 0

    for i, j in zip(s, t):
        if i == j:
            count_similar_char += 1
        else:
            break
    total_len = len(s) + len(t)

    if total_len <= 2 * count_similar_char + k and total_len % 2 == k % 2 or total_len < k:
        return "Yes"
    else:
        return "No"


if __name__ == '__main__':
    initial_string = input()
    desired_string = input()
    number_of_operations = int(input())

    result = append_and_delete(initial_string, desired_string, number_of_operations)

    print(result + '\n')
