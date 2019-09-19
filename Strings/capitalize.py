# https://www.hackerrank.com/challenges/capitalize/problem

# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the solve function below.
def solve(s):
    s = s.split(' ')
    res = []
    for word in s:
        res.append(word.capitalize())

    return ' '.join(res)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
