#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


# Complete the makeAnagram function below.
def makeAnagram(a, b):
    arr = [0]*26
    for c in a:
        arr[ord(c) - ord('a')] += 1

    for c in b:
        index = ord(c) - ord('a')
        arr[index] -= 1

    sum = 0
    for freq in arr:
        sum += abs(freq)

    return sum

if __name__ == '__main__':
    a = input()

    b = input()

    res = makeAnagram(a, b)

    print(res)
