#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the fairRations function below.
def fairRations(B):
	sum = 0
	for b in B:
		sum += b

	if sum % 2 != 0:
		print("NO")
	else:
		count = 0
		for i in range(len(B) - 1):
			b = B[i]
			if b % 2 != 0:
				B[i] += 1
				B[i + 1] += 1
				count += 2
		print(count)


if __name__ == '__main__':
    N = int(input())

    B = list(map(int, input().rstrip().split()))

    fairRations(B)