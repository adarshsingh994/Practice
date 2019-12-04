#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the howManyGames function below.
def howManyGames(p, d, m, s):
    # Return the number of games you can buy
    curBalance = s
    count = 0
    while curBalance > 0:
        curBalance -= p
        if curBalance >= 0:
            count += 1
            diff = p - d
            if diff > m:
                p = diff
            else:
                p = m

    print(count)
        
        
        

if __name__ == '__main__':
    pdms = input().split()

    p = int(pdms[0])

    d = int(pdms[1])

    m = int(pdms[2])

    s = int(pdms[3])

    howManyGames(p, d, m, s)
