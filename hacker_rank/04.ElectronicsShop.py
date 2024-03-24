#!/bin/python3

import os
import sys

# https://www.hackerrank.com/challenges/electronics-shop/problem?isFullScreen=true
# Complete the getMoneySpent function below.
#

def getMoneySpent(keyboards, drives, b):
    combinations = []
    # Create all combinations using double repetition
    for k in keyboards:
        for d in drives:
            s = k + d
            if s <= b:
                combinations.append(s)
    # Create over 2 list of combinations using itertools.product
    # from itertools import product
    # combinations = list(product(keyboards, drives))

    if len(combinations) == 0:
        return -1
    return max(combinations)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
