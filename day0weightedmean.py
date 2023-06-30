# https://www.hackerrank.com/challenges/s10-weighted-mean/problem
#!/bin/python3

import math
import os
import random
import re
import sys
from operator import mul
from itertools import starmap

def weightedMean(X, W):
    #X = input().split(" ")
    #W = input().split(" ")
    print(f"{sum(starmap(mul, zip(X,W))) / sum(W):.1f}")
# my solution is on Line 15 :-)
  
if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    weights = list(map(int, input().rstrip().split()))

    weightedMean(vals, weights)
