#!/bin/python3

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/bon-appetit/problem?isFullScreen=true
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#

def bonAppetit(bill, k, b):
    # sum list
    portion_anna = [v for i, v in enumerate(bill) if i != k]
    b2 = b - int(sum(portion_anna) / 2)
    result = 'Bon Appetit' if b2 == 0 else b2
    print(result)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
