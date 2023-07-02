#!/bin/python3

import math
import os
import random
import re
import sys
from statistics import median

# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.

def quartiles(arr):
    arr.sort() 
    q1=median(arr[: len(arr)//2]) 
    q2=median(arr)     
    q3=median(arr[len(arr)//2 *-1:]) 
    return list(map(int,[q1,q2,q3]))

# my code is above this line
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
