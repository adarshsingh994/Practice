#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k):
    items = 0
    expenditure = 0
    for price in sorted(prices):
        expenditure += price
        if(expenditure > k):
            expenditure -= price
            break
        items += 1
    return items

if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    print (result)
