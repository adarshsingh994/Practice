#!/bin/python3

import math
import os
import random
import re
import sys

# get length of integer (faster than len(str(num)))
# digits = int(math.log10(n))+1
# Complete the separateNumbers function below.
def separateNumbers(s):
    digits = 1
    isBeautiful = False
    firstDigit = -1
    while digits < len(s):
        isBeautiful = False
        position = 0
        toFind = -1
        digitsInToFind = digits
        while position < (len(s) - digitsInToFind + 1):
            val = int(s[position : (position + digitsInToFind)])
            # print("To Find: " + str(toFind))
            # print("Digits in toFind: " + str(digitsInToFind))
            # print("Val: " + str(val))

            if toFind != -1:
                if val == toFind:
                    isBeautiful = True
                else:
                    isBeautiful = False
                    break
            else:
                firstDigit = val
            toFind = val + 1
            position += digitsInToFind
            if toFind == 0:
                digitsInToFind = 1
            else:
                digitsInToFind = int(math.log10(toFind))+1

            digitsRemaining = len(s) - position
            if digitsRemaining > 0 and digitsRemaining < digitsInToFind:
                isBeautiful = False
                break

        if isBeautiful == True:
            break
        digits += 1
    if isBeautiful:
        print("YES " + str(firstDigit))
    else:
        print("NO")

if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)


        # 4294967295
        # 4294967296
        # 42949672
        
        # A-4294967295