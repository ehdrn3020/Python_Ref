#!/bin/python3

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/drawing-book/problem?isFullScreen=true
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    # get start front
    # get start end
    # compare lower number
    return min(p//2, n//2 - p//2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
