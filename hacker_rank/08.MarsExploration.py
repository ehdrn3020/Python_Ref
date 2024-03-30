#!/bin/python3

import os

# Functions to find the number of incorrect characters by comparing strings of different lengths
# https://www.hackerrank.com/challenges/mars-exploration/problem?isFullScreen=true

def marsExploration(s):
    return sum(int(cs != cr) for cs, cr in zip(s, "SOS" * (len(s) // 3)))

    # without zip
    # sum(s[i] != 'SOS'[i%3] for i in range(len(s)))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
