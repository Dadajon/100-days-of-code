
def factorial(n):
    """
    Write a factorial function that takes a positive integer, N as a parameter and prints the result of N! (N factorial).
    
    :param n: input integer
    :return: factorial value
    """
    if n == 0 or n == 1:
        return 1
    else:
        return factorial(n - 1) * n


if __name__ == '__main__':
    n = int(input())

    result = factorial(n)

    print(str(result) + '\n')
