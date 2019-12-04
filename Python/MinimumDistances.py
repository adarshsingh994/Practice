#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
    posMap = dict()
    minDistance = 100000
    for i in range(len(a)):
        if a[i] in posMap:
            val = i - posMap[a[i]]
            if minDistance > val:
                minDistance = val
        else:
            posMap[a[i]] = i
    if minDistance == 100000:
        print("-1")
    else:
        print(minDistance)

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    minimumDistances(a)


