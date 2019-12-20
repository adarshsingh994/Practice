#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the happyLadybugs function below.
def happyLadybugs(b):
    freqDict = Counter(b)
    is_present = False
    for keyVal in freqDict:
        if keyVal == '_':
            is_present = True
        elif freqDict[keyVal] == 1:
            return 'NO'
    if is_present == True:
        return 'YES'
    else:
        string = ""
        for key in freqDict:
            for c in range(freqDict[key]):
                string += key
        if b == string:
            return 'YES'
        else:
            return 'NO'
    

if __name__ == '__main__':
    g = int(input())

    for g_itr in range(g):
        n = int(input())

        b = input()

        result = happyLadybugs(b)

        print(result)
