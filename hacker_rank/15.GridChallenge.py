#!/bin/python3

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/grid-challenge/problem?isFullScreen=true

#- 행과 열을 바꾸는 작업을 전치(transpose)
#- `zip(*grid)`는 `grid`의 각 요소를 개별 인자로 풀어서 전달
#- `*` 연산자는 리스트의 각 요소를 풀어서 개별 인자로 전달하는 역할#
#

def gridChallenge(grid):
    # ['eba'] -> ['e','b','a'] 변환
    for i in range(len(grid)):
        grid[i] = sorted(list(grid[i]))
    # 전치 작업을 실행
    # grid = ["eba", "fgh", "olm"]
    # [('e', 'f', 'o'), ('b', 'g', 'l'), ('a', 'h', 'm')]
    for x in list(zip(*grid)):
        if list(x) != sorted(x):
            return "NO"
    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
