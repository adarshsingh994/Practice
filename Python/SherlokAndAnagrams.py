#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    # Run the loop length of string times
    subStringList = []
    for i in range(len(s) - 1):
        for j in range(len(s) - i):
            possibleSubString = s[j : j + i + 1]
            subStringList.append(''.join(sorted(possibleSubString)))
    counted = Counter(subStringList)

    # Count combinations
    total = 0
    for subStr,freq in counted.items():
        combinations = int((freq * (freq - 1)) / 2)
        total = total + combinations
    
    return total
                
                

if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()
        result = sherlockAndAnagrams(s)
