#!/bin/python3
import os
import sys

# Complete the handshake function below.
def handshake(n):
    sum = 0
    if n <= 1:
        return 0
    for i in range(1, n):
        sum = sum + (n-i)
    return sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = handshake(n)

        fptr.write(str(result) + '\n')

    fptr.close()