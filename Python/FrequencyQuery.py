#!/bin/python3

import math
import os
import random
import re
import sys

freqMap = dict()
freqMap2 = dict()

# Complete the freqQuery function below.
def freqQuery(instData):
    inst = instData[0]
    data = instData[1]
    
    # Process the output
    if inst == 1:
        if data in freqMap:
            freq = freqMap[data]
            val = freqMap2[freq] - 1
            if(val == 0):
                del freqMap2[freq]
            else:
                freqMap2[freq] = val
            newFreq = freq + 1
            freqMap[data] = newFreq
            if newFreq in freqMap2:
                freqMap2[newFreq] = freqMap2[newFreq] + 1
            else:
                freqMap2[newFreq] = 1
        else:
            freqMap[data] = 1
            if 1 in freqMap2:
                freqMap2[1] = freqMap2[1] + 1
            else:
                freqMap2[1] = 1
    elif inst == 2:
        if data in freqMap:
            freq = freqMap[data]

            val = freqMap2[freq] - 1
            if val == 0:
                del freqMap2[freq]
            else:
                freqMap2[freq] = val
            newFreq = freq - 1

            if newFreq == 0:
                del freqMap[data]
            else:
                freqMap[data] = newFreq
            if newFreq in freqMap2:
                freqMap2[newFreq] = freqMap2[newFreq] + 1
            else:
                freqMap2[newFreq] = 1
                
    elif inst == 3:
        if data in freqMap2:
            if freqMap2[data] <= 0:
                return 0
            else:
                return 1
        else:
            return 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input().strip())
    for _ in range(q):
        result = freqQuery(list(map(int, input().rstrip().split())))
        if result != None:
            fptr.write(str(result) + '\n')

    fptr.close()
