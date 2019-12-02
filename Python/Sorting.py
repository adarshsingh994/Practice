#!/bin/python3

import math
import os
import random
import re
import sys

def swap(aj, aj1):
    temp = aj
    aj = aj1
    aj1 = temp
    return aj, aj1

# Complete the countSwaps function below.
def countSwaps(a):
    swaps = 0
    min = 2000000
    max = 0
    for i in range(n): 
        for j in range(n - 1):
            # Swap adjacent elements if they are in decreasing order
            if a[j] < min:
                min = a[j]
            if a[j + 1] < min:
                min = a[j + 1]

            if a[j] > max:
                max = a[j]
            if a[j + 1] > max:
                max = a[j + 1]
                
            if a[j] > a[j + 1]:
                aj, aj1 = swap(a[j], a[j + 1])
                a[j] = aj
                a[j + 1] = aj1
                swaps += 1
    print ('Array is sorted in ' + str(swaps) + ' swaps.')
    print('First Element: ' + str(min))
    print ('Last Element: ' + str(max))

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
