#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the primality function below.
def primality(p):
	if p < 2:
		return False
	elif p <= 3:
		return True
	elif p % 2 == 0 or p % 3 == 0:
		return False
	else:
		for i in range(3, int(math.sqrt(p)+1), 2):
			if p % i == 0:
				return False
		return True


if __name__ == '__main__':
    p = int(input())

    for p_itr in range(p):
        n = int(input())

        result = primality(n)

        if result == True:
        	print("Prime")
        else:
        	print("Not prime")