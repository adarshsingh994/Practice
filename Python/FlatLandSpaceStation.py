#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
	if n == len(c):
		print(0)
	else:
		maxDis = 0
		for city in range(n):
			minDis = 100000
			for station in c:
				dis = abs(station - city)
				if dis < minDis:
					minDis = dis
			if minDis > maxDis:	
				maxDis = minDis
		print (maxDis)


if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    flatlandSpaceStations(n, c)
