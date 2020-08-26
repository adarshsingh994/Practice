#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the missingNumbers function below.
def missingNumbers(arr, brr):
    printedList = dict()
    referenceList = []
    for b in brr:
        referenceList.append(b)
        if b in arr:
            referenceList.remove(b)
            arr.remove(b)

    for ddd in sorted(referenceList):
        if ddd not in printedList:
            print(ddd, end=" ")
            printedList[ddd] = True
    

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    brr = list(map(int, input().rstrip().split()))

    missingNumbers(arr, brr)
