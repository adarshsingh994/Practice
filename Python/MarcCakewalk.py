#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marcsCakewalk function below.
def marcsCakewalk(calorie):
	summation = 0
	for i in range(len(calorie)):
		summation = summation + math.pow(2, i) * calorie[i]
	print(int(summation))

if __name__ == '__main__':
    n = int(input())

    calorie = list(map(int, input().rstrip().split()))

    marcsCakewalk(sorted(calorie, reverse = True))