#!/bin/python3

import math
import os
import random
import re
import sys

from itertools import count, zip_longest
def workbook(n,k,a):
    page=count(1)
    print (sum([len([1 for probs in zip_longest(*[iter(range(1, num_chpt_probs+1))]*k) if next(page) in probs]) for num_chpt_probs in a]))


if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    workbook(n, k, arr)