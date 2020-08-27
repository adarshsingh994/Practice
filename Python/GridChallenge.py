#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gridChallenge function below.
def gridChallenge(grid, n):
    for i in range(0, len(grid[0])):
        for j in range(0, n):
            if j != 0:
                if ord(grid[j][i]) < ord(grid[j - 1][i]):
                    print ("NO")
                    return

    print("YES")
                    
            
        

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(sorted(grid_item))

        gridChallenge(grid, n)
