#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
	t = int(input())
	for _ in range(t):
		s = int(input())
		if s % 7 < 2:
			print ('Second')
		else:
			print ('First')
