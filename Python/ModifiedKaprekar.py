#!/bin/python3

import math
import os
import random
import re
import sys

def isKaprekar(num):
    if num == 1:
        return True
    elif num == 2:
        return False
    elif num == 3:
        return False
    else:
        square = num * num
        strSquare = str(square)
        r = strSquare[-len(str(num)):]
        l = strSquare[:len(strSquare) - len(str(num))]
        #print(str(l) + " : " + str(r))
        if int(r) + int(l) == num:
            return True
        else:
            return False

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    list = []
    for i in range(p, q+1):
        if isKaprekar(i):
            list.append(i)
    if(len(list) == 0):
        print("INVALID RANGE")
    else:
        print(*list)

if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
