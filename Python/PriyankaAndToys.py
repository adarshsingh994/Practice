#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the toys function below.
def toys(w):
	count = 1
	dick = w[0]
	for i in range(1, len(w)):
		if w[i] > (dick + 4):
			count = count + 1
			dick = w[i]
	print(count)


if __name__ == '__main__':
    n = int(input())

    w = list(map(int, input().rstrip().split()))

    result = toys(sorted(w))