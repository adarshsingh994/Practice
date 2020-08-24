#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximizingXor function below.
def maximizingXor(l, r):
	maxXor = 0
	for i in range(l, r + 1):
		for j in range(i, r + 1):
			curXor = i ^ j
			if curXor > maxXor:
				maxXor = curXor
	print(maxXor)

if __name__ == '__main__':
    l = int(input())

    r = int(input())

    maximizingXor(l, r)