#!/bin/python3

import math
import os
from collections import Counter
import random
import re
import sys

# Complete the sumXor function below.
def sumXor(n):
    if n == 0:
        return 1
    binary = bin(n).replace("0b", "")
    cccc = Counter(binary)["0"]
    return pow(2, cccc)
if __name__ == '__main__':
    n = int(input().strip())

    print(sumXor(n))
