#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    a = s.split(" ")
    b = []
    for i in a:
        i = str(i)
        d = i.capitalize()
        b.append(d)
    c = ' '.join(b)
    return c
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
