
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, r):
    triplets = 0
    secondTermMap = dict()
    thirdTermMap = dict()

    for element in arr:
        triplets += thirdTermMap.get(element, 0)
        if element in secondTermMap:
            thirdTermMap[element*r] = thirdTermMap.get((element*r), 0) + secondTermMap[element]
        secondTermMap[element*r] = secondTermMap.get((element*r), 0) + 1
    return triplets

if __name__ == '__main__':
    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    print (ans)
