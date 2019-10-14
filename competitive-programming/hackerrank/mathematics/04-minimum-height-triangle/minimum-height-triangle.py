#!/bin/python3
import sys

def lowestTriangle(base, area):
    height = int(round(area*2/base))
    new_area = int(round(height*base/2))
    if new_area >= area:
        return height
    else:
        return height + 1

base, area = input().strip().split(' ')
base, area = [int(base), int(area)]
height = lowestTriangle(base, area)
print(height)