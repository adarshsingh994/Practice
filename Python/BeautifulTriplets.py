#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulTriplets function below.
def beautifulTriplets(d, arr):
        triplets = 0
        for i in range(len(arr)):
            one = arr[i]+d
            two = arr[i]+2*d
            if two > arr[len(arr) - 1]:
                break
            
            if one in arr and two in arr:
                triplets+=1
        print (triplets)

if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    arr = list(map(int, input().rstrip().split()))

    beautifulTriplets(d, arr)
