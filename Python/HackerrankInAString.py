#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hackerrankInString function below.
def hackerrankInString(s):
    hackerrank = ['h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k']
    c = 0
    for character in s:
        if character == hackerrank[c]:
            c += 1
            if c== 10:
                return 'YES'
    if c == 10:
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        print(result)
