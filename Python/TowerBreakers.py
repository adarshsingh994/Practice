#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the towerBreakers function below.
def towerBreakers(n, m):
    if m==1:
        return 2
    if n%2==0:
        return 2
    else:
        return 1

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        print (towerBreakers(n, m))
