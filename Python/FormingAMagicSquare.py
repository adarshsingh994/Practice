#!/bin/python3

import math
import os
import random
import re
import sys
import copy 

def rotateMatrix(mato, N):
    mat = copy.deepcopy(mato)
    for x in range(0, int(N / 2)): 
        for y in range(x, N-x-1):   
            temp = mat[x][y] 
            mat[x][y] = mat[y][N-1-x] 
            mat[y][N-1-x] = mat[N-1-x][N-1-y] 
            mat[N-1-x][N-1-y] = mat[N-1-y][x] 
            mat[N-1-y][x] = temp
    return mat

def reflectMatrixThroughCenter(mato, N):
    mat = copy.deepcopy(mato)
    if N%2 != 0:
        for i in range(N):
            for j in range(int(N/2)):
                temp = mat[i][j]
                mat[i][j] = mat[i][N - 1 - j]
                mat[i][N - 1 - j] = temp
        return mat
    else:
        return None

def getCost(mat, refMat):
    cost = 0
    for i in range(3):
        for j in range(3):
            cost = cost + abs(mat[i][j] - refMat[i][j])
    return cost

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    rotated = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
    minCost = 999999
    currentCost = getCost(s, rotated)
    if minCost > currentCost:
        minCost = currentCost
    currentCost = getCost(s, reflectMatrixThroughCenter(rotated, 3))
    if minCost > currentCost:
        minCost = currentCost
    
    for i in range(4):
        rotated = rotateMatrix(rotated, 3)
        currentCost = getCost(s, rotated)
        if minCost > currentCost:
            minCost = currentCost
        currentCost = getCost(s, reflectMatrixThroughCenter(rotated, 3))
        if minCost > currentCost:
            minCost = currentCost
    return minCost

if __name__ == '__main__':
    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    print(formingMagicSquare(s))
