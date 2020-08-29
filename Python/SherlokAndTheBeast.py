#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the decentNumber function below.
def decentNumber(n):
	order = []
	while(n != 0):
		if n < 3:
			return (-1)

		if n%3 < n%5 or n%3 == n%5:
			n = n - 3
			order.append(3)
		else:
			n = n - 5
			order.append(5)
	return sorted(order)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = decentNumber(n)
        if result == -1:
        	print(-1)
        else:
        	print(result)
        	for j in result:
        		for k in range(j):
        			if j == 3:
       					print(5, end="")
       				else:
       					print(3, end="")
       		print("")
       	# 555555555555555
       	# 333333333333333
