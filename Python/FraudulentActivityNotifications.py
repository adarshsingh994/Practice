#!/bin/python3

import math
import os
import random
import re
import sys
import statistics
from collections import deque

def median(v, d):
    count = 0
    if d%2==0:
        m1 = None
        m2 = None
        for i in range(len(v)):
            count += v[i]
            if count == d/2 and m1 is None:
                m1 = i
            if count == d/2 + 1:
                m2 = i
                break
        return (m1 + m2)/2
    else:
        for i in range(len(v)):
            count += v[i]
            if count > d/2:
                return i
    return -1

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    dq = deque(expenditure[: d])
    v = [0]*201
    for n in dq:
        v[n] += 1
    count = 0
    for current in expenditure[d:]:
        if current >= median(v, d)*2:
            count += 1
        v[current] += 1
        dq.append(current)
        v[dq.popleft()] -= 1
    return count
            
if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    print(result)

















'''notifications = 0
    sum = 0
    mode = None
    maxFreq = 0
    freqMap = dict()
    
    for i in range(len(expenditure)):
        if i < d:
            sum += expenditure[i]
            freq = freqMap.get(expenditure[i], 0) + 1
            freqMap[expenditure[i]] = freq
            if freq > maxFreq:
                maxFreq = freq
                mode = expenditure[i]
        else:
            if expenditure[i] >= (2 * (mode + ((2/3) * ((sum/d) - mode)))):
                notifications += 1
            sum -= expenditure[i - d]
            sum += expenditure[i]

            freqMap[expenditure[i - d]] = max(freqMap[expenditure[i - d]] - 1, 0)
            freqMap[expenditure[i]] = freqMap.get(expenditure[i], 0) + 1







                

                # for i in range(d, len(expenditure)):
      #  if expenditure[i] >= 2 * statistics.median(sorted(expenditure[i - d : i])):
       #     notifications += 1
    # return notifications
    return notifications'''
