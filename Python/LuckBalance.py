#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    dick = 0
    pussy = 0
    for condom in contests:
        if(condom[1] == 1):
            pussy = pussy + 1
            if(pussy <= k):
                dick = dick + condom[0]
            else:
                dick = dick - condom[0]
        else:
            dick = dick + condom[0]

    print(dick)

if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    luckBalance(k, sorted(contests, reverse=True))