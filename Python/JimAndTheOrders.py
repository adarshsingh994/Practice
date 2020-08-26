#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jimOrders function below.
def jimOrders(orders):
    exectutionOrder = dict()
    for i in range(len(orders)):
        variab = orders[i][0] + orders[i][1]
        if(variab in exectutionOrder):
            exectutionOrder[variab].insert(0, i)
            exectutionOrder[variab] = sorted(exectutionOrder[variab])
        else:
            exectutionOrder[variab] = [i]
    for vall in sorted(exectutionOrder.keys()):
        for kk in exectutionOrder[vall]:
            print(kk + 1, end =" ")
    

if __name__ == '__main__':
    n = int(input())

    orders = []

    for _ in range(n):
        orders.append(list(map(int, input().rstrip().split())))

    jimOrders(orders)
