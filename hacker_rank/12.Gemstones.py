#!/bin/python3

import math
import os
import random
import re
import sys

# Strings 문제
# 젬스톤 찾기, 젬스톤이란 모든 배열에 포함되어있는 문자
# https://www.hackerrank.com/challenges/gem-stones/problem?isFullScreen=true

def gemstones(arr):
    # arr = ['abcdde', 'baccd', 'eeabg']
    # 첫 번째 문자열을 집합으로 변환
    common_chars = set(arr[0])
    # 나머지 문자열 집합과의 교집합을 구함
    for string in arr[1:]:
        common_chars &= set(string)
        # OR common_chars.intersection(set(string))
    return len(list(common_chars))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
