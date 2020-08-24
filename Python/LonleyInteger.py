#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the lonelyinteger function below.
def lonelyinteger(a):
	d = dict()
	ccc = 0
	for aaa in a:
		if aaa in d:
			d.pop(aaa)
			ccc = ccc - 1
		else:
			d[aaa] = True
			ccc = ccc + 1
	print(list(d.keys())[0])


if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    lonelyinteger(a)