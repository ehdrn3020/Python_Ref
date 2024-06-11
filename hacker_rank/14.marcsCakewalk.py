#!/bin/python3

# Greedy
# https://www.hackerrank.com/challenges/marcs-cakewalk/problem?isFullScreen=true
# 2의 0승, 2의 1승, 2의 2승 ... len(calorie) 와 calorie 배열 요소의 곱 중 최소합계 값 구하기

import os

def marcsCakewalk(calorie):
    result = []
    calorie.sort(reverse=True)
    for i, cal in enumerate(calorie):
        result.append((2**i) * cal)
    return sum(result)
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    calorie = list(map(int, input().rstrip().split()))

    result = marcsCakewalk(calorie)

    fptr.write(str(result) + '\n')

    fptr.close()
