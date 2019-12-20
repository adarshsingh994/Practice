#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the strangeCounter function below.
def strangeCounter(t):
	rem = 3
	while t > rem:
		t = t-rem
		rem *= 2

	print(rem-t+1)


if __name__ == '__main__':
    t = int(input())

    strangeCounter(t)