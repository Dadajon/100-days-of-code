from icecream import ic


def divisors(n):
    """For each testcase, return number of divisors

    Args:
        n ([int]): integer number

    Returns:
        [int]: number of divisors of 'n' that are divisible by 2
    """    
    # # this approach is too slow
    # cnt_divisors = len([i for i in range(2, n+1, 2) if not n%i])

    if n % 2: # odd
        return 0
    else: # even
        n /= 2
        cnt_divisors = 1
        p = 2
        while p <= n:
            if p * p > n: p = n
            e = 0
            while n % p == 0:
                e += 1
                n /= p
            cnt_divisors *= e + 1
            p += 1
        return cnt_divisors


def main():
    t = int(input().strip())
    
    for t_itr in range(t):
        n = int(input().strip())
        result = divisors(n)
        ic(str(result))


if __name__ == '__main__':
    main()
