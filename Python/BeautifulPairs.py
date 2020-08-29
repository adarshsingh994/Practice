#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulPairs function below.
def beautifulPairs(n, A, B):
	result = 0
	rejectindex = dict()
	for i in range(0, n):
		for j in range(0, n):
			if j not in rejectindex:
				if A[i] == B[j]:
					result = result + 1
					rejectindex[j] = True
					break
	if result < n:
		result = result + 1
	elif result == n:
		result = result - 1
	return result



if __name__ == '__main__':
    n = int(input())

    A = list(map(int, input().rstrip().split()))

    B = list(map(int, input().rstrip().split()))

    result = beautifulPairs(n, A, B)

    print(result)