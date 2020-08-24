#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoArrays function below.
def twoArrays(k, A, B):
    for ai in range(len(A)):
        yes = False
        for bi in range(ai, len(B)):
            if (A[ai] + B[bi]) >= k:
                yes = True
                break
        if yes == False:
            print("NO")
            return
    print("YES")


if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        A = list(map(int, input().rstrip().split()))

        B = list(map(int, input().rstrip().split()))

        twoArrays(k, sorted(A, reverse=False), sorted(B, reverse=True))