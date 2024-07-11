#!/bin/python3

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem?isFullScreen=true
# Complete the 'climbingLeaderboard' function below.
#
# 두 개의 포인터를 사용하여 기존 점수판과 플레이어의 점수를 비교하는 접근 방식을 사용
# 두 번의 반복문을 통해 비교

def climbingLeaderboard(ranked, player):
    # 기존 점수판의 중복을 제거하여 고유한 점수 리스트를 생성
    unique_ranked = sorted(set(ranked), reverse=True)
    result = []
    n = len(unique_ranked)

    # 각 플레이어의 점수를 처리
    for score in player:
        # 새로운 점수에 대해 고유한 점수 리스트와 비교
        while n > 0 and score >= unique_ranked[n - 1]:
            n -= 1
        result.append(n + 1)

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
