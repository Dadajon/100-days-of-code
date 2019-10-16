#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    """
    Complete the countApplesAndOranges function in the editor below. It should print the number of apples and oranges that land on Sam's house, each on a separate line.

    :param s: integer, starting point of Sam's house location.
    :param t: integer, ending location of Sam's house location.
    :param a: integer, location of the Apple tree.
    :param b: integer, location of the Orange tree.
    :param apples: integer array, distances at which each apple falls from the tree.
    :param oranges: integer array, distances at which each orange falls from the tree.
    :return: determine how many apples and oranges will fall on Sam's house [s,t]
    """
    
    apple_count = 0
    orange_count = 0

    # distance from apple tree
    for i in range(len(apples)):
        temp = a + apples[i]
        if temp in range(s, t+1):
            apple_count += 1

    # distance from orange tree
    for i in range(len(oranges)):
        temp = b + oranges[i]
        if temp in range(s, t+1):
            orange_count += 1
            
    print(apple_count)
    print(orange_count)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
