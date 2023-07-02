#!/bin/python3

import math
import os
import random
import re
import sys
import statistics

#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def stdDev(arr):
    # Print your answers to 1 decimal place within this function
    mean=sum(arr)/len(arr)
    diff_sqr=[]
    for item in arr:
        diff_sqr.append((item-mean)**2)
    
    print(round((sum(diff_sqr)/len(arr))**(1/2),1))

# my code is above this line.
if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    stdDev(vals)
