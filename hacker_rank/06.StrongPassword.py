#!/bin/python3

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/strong-password/problem?isFullScreen=true
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    condition = ["0123456789",
                 "abcdefghijklmnopqrstuvwxyz",
                 "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                 "!@#$%^&*()-+"]

    result = [0, 0, 0, 0]
    for item in password:
        if item in condition[0]:
            result[0] = 1
        if item in condition[1]:
            result[1] = 1
        if item in condition[2]:
            result[2] = 1
        if item in condition[3]:
            result[3] = 1
        if all(result):
            break

    # first check the length of password, not enough return 6 - len(password)
    # sencond check the condition 3(digit, upper, lower, special)
    return max(4 - sum(result), 6 - len(password))

    ## Use Regex
    # result = 0
    # if len(re.findall("[0-9]", password)) == 0:
    #     result += 1
    # if len(re.findall("[A-Z]", password)) == 0:
    #     result += 1
    # if len(re.findall("[!@#$%^&*()-+-]", password)) == 0:
    #     result += 1
    # if len(re.findall("[a-z]", password)) == 0:
    #     result += 1
    # if n + result < 6:
    #     return 6 - n
    # return cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
