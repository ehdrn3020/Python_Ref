#!/bin/python3

import math
import os
import random
import re
import sys

# Make sure a particular string contains all the alphabets
# https://www.hackerrank.com/challenges/pangrams/problem?isFullScreen=true

def pangrams(s):
    alphabet_string = 'abcdefghijklmnopqrstuvwxyz'
    ss = s.lower()
    # check s, involved { a-z, A-Z, space}
    for char in alphabet_string:
        if char not in ss and char != ' ':
            print(char)
            return "not pangram"
    return "pangram"

    ## Another solved ##
    # Using ASCII code - for i in range(97, 123):
    # Using Set - return "pangram" if len(set(s.lower().replace(' ',''))) == 26 else "not pangram"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
