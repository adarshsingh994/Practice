#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
	minDiff = abs(arr[0] - arr[1])
	for i in range(1, len(arr) - 1):
		minCur = abs(arr[i] - arr[i + 1])
		if minCur < minDiff:
			minDiff = minCur
	print(minDiff)


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    minimumAbsoluteDifference(sorted(arr))