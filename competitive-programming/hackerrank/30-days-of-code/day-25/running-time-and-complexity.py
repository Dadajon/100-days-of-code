import math


def is_prime(n):
    """
    A prime is a natural number greater than 1 that has no positive divisors other than 1 and itself.
    Given a number, n, determine and print whether it's 'Prime' or 'Not prime'.

    :param n: an integer, n, to be tested for primality
    :return: print whether n is 'Prime' or 'Not prime' on a new line
    """
    if n <= 1:
        return False

    sqrt_n = int(math.sqrt(n))
    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            return False

    return True


if __name__ == "__main__":
    num_test_cases = int(input())

    for _ in range(num_test_cases):
        n = int(input())
        if is_prime(n):
            print("Prime")
        else:
            print("Not prime")