#!/bin/python3

import math
import os
import random
import re
import sys

# Get weight map for the inputted string
def getWeightMap(s):
    currentChar = ''
    weightMap = dict()
    currentWeight = 0
    for character in s:
        if currentChar == '':
            currentChar = character
            weight = ord(character) - 96
            currentWeight = weight
        else:
            if character == currentChar:
                weight = ord(character) - 96
                currentWeight += weight
            else:
                weight = ord(character) - 96
                currentChar = character
                currentWeight = weight
        weightMap[currentWeight] = True
    return(weightMap)

if __name__ == '__main__':
    s = input()

    weightMap = getWeightMap(s)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        if queries_item in weightMap:
            print("Yes")
        else:
            print("No")