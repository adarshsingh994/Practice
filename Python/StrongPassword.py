#!/bin/python3

import math
import os
import random
import re
import sys

def getCharType(c):
	# Get character type
	val_ascii = ord(c)
	# number type
	if val_ascii >= 48 and val_ascii <= 57:
		return 'n'
	# lower case type
	elif val_ascii >= 97 and val_ascii <= 122:
		return 'l'
	# upper case type
	elif val_ascii >= 65 and val_ascii <= 90:
		return 'u'
	# special character type
	else:
		return 's'

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    if n <= 3:
    	return (6 - n)

    dictionary = {
    'n' : False
    , 'u' : False
    , 'l' : False
    , 's' : False
    }

    counter = 0

    for c in password:
    	charType = getCharType(c)
    	if dictionary[charType] == False:
    		dictionary[charType] = True
    		counter += 1

    atLeast = 4 - counter
    if n < 6:
    	if (6 - n) > atLeast:
    		return (6 - n)
    	else:
    		return atLeast


    return atLeast

if __name__ == '__main__':
    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    print(answer)