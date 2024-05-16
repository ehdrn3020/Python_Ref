#!/bin/python3

import os


# reverse list
# get ascii code each list
# compare 2 array's absolute differences, list and reversed list
#
# https://www.hackerrank.com/challenges/funny-string/problem?isFullScreen=true

def funnyString(s):
    a, b = [], []
    s0 = s[::-1]
    for i in range(len(s) // 2):
        a.append(abs(ord(s[i]) - ord(s[i + 1])))
        b.append(abs(ord(s0[i]) - ord(s0[i + 1])))
    return "Funny " if a == b else "Not Funny"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
