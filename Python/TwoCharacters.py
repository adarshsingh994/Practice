#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

def validate(cpy):
    for i in range(len(cpy)-1):
        if cpy[i] == cpy[i+1]:
            return False
    return True

# Complete the alternate function below.
def alternate(s):
    st = list(set(s))
    max_len = 0
    for x in range(len(st)):
        for y in range(x+1, len(st)):
            cpy = [c for c in s if c==st[x] or c==st[y]]
            if validate(cpy):
                max_len = max(max_len, len(cpy))
    return max_len
                    

if __name__ == '__main__':
    l = int(input().strip())

    s = input()

    result = alternate(s)

    print(result)
