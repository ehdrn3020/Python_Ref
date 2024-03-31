#!/bin/python3

import math
import os
import random
import re
import sys

# Find specific characters in multiple strings.
# https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem?isFullScreen=true

def hackerrankInString(s):
    # using pop
    word = list('hackerrank')
    for i in s:
        if not word:
            return 'YES'
        if i in word[0]:
            word.pop(0)
    return 'NO' if word else 'YES'
    # using regex
    # return "YES" if re.match(r".*h.*a.*c.*k.*e.*r.*r.*a.*n.*k.*", s) else "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
