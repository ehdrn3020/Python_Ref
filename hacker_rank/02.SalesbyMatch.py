#!/bin/python3

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/sock-merchant/problem?isFullScreen=true
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # How many times each element comes out with collections.Counter
    from collections import Counter
    count_dict = Counter(ar)
    # Dict type is possible comprehension
    dict_result = dict((k, v // 2) for k, v in count_dict.items() if v > 1)
    return sum(dict_result.values())

    # Summary
    # sum(i//2 for i in collections.Counter(ar).values())

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
