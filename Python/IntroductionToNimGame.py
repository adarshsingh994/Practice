#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the nimGame function below.
def nimGame(pile):
    xorr = 0
    for p in pile:
        xorr = xorr^p
    if xorr == 0:
        return "Second"
    else:
        return "First"

if __name__ == '__main__':
    g = int(input())

    for g_itr in range(g):
        n = int(input())

        pile = list(map(int, input().rstrip().split()))

        print (nimGame(pile))
