#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flippingBits function below.
def flippingBits(n):
	flipped = ""
	for i in range(len(n)):
		if n[i] == '1':
			flipped = flipped + "0"
		elif n[i] == '0':
			flipped = flipped + "1"
	print(int(flipped, 2))
if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        n = int(input())

        flippingBits('{:032b}'.format(n))