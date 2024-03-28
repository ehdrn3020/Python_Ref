#!/bin/python3

import os
#  String Unicode Rotate
# ord('z') / chr(112)
# https://www.hackerrank.com/challenges/caesar-cipher-1/problem?isFullScreen=true

def caesarCipher(s, k):
    encrypted = ''

    for char in s:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            encrypted += chr((ord(char) - base + k) % 26 + base)
        else:
            encrypted += char
    return encrypted

    # OR

    # result = ''
    # for c in s:
    #     if c.isalpha():
    #         rotate = k
    #         while rotate > 0:
    #             if c == 'z' or c == 'Z':
    #                 c = chr(ord(c) - 25)
    #             else:
    #                 c = chr(ord(c) + 1)
    #             rotate -= 1
    #     result += c
    # return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
