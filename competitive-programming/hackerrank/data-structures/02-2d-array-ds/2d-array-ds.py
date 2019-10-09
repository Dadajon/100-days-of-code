#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def _get_hourglass_sum_(matrix, row, col):
    result = 0
    result += matrix[row-1][col-1]
    result += matrix[row-1][col]
    result += matrix[row-1][col+1]
    result += matrix[row][col]
    result += matrix[row+1][col-1]
    result += matrix[row+1][col]
    result += matrix[row+1][col+1]
    return result

def hourglassSum(arr):
    max_hourglass_sum = -63
    for i in range(1,5):
        for j in range(1,5):
            current_hourglass_sum = _get_hourglass_sum_(arr,i,j)
            if current_hourglass_sum > max_hourglass_sum:
                max_hourglass_sum = current_hourglass_sum
    return max_hourglass_sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result))

    fptr.close()