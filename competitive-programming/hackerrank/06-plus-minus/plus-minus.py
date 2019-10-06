#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    pos = sum(map(lambda x: x>0, arr))/len(arr)
    neg = sum(map(lambda x: x<0, arr))/len(arr)
    zeros = sum(map(lambda x: x==0, arr))/len(arr)
    print("{0:1.5f}\n{1:1.5f}\n{2:1.5f}".format(pos, neg, zeros))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
