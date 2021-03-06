#!/bin/python3

import math
import os
from functools import reduce
import random
import re
import sys

# Complete the misereNim function below.
def misereNim(s):
    if (set(s)=={1}) and n%2==1:
        return 'Second'
    elif (set(s)=={1}) and n%2==0:
        return 'First'
    elif reduce((lambda x,y:x^y),s):
        return 'First'
    else:
        return 'Second'

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        s = list(map(int, input().rstrip().split()))

        print(misereNim(s))
