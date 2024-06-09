#!/bin/python3
import os

# Greedy
# https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem?isFullScreen=true
# 임의의 두 요소 사이의 최소의 절대값 차이를 나타내는 정수를 반환
def minimumAbsoluteDifference(arr):
	arr.sort()
	return min(( abs( arr[i+1] - arr[i] ) for i in range(len(arr)-1) ))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
