#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the equalizeArray function below.
def equalizeArray(arr):
    maxFreq = 0
    freqMap = {}
    for ar in arr:
        if ar in freqMap:
            freqMap[ar] += 1
        else:
            freqMap[ar] = 1

        if freqMap[ar] > maxFreq:
            maxFreq = freqMap[ar]

    print(len(arr) - maxFreq) 
    

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    equalizeArray(arr)
