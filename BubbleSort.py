#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    count = 0
    for i in range(len(a)):
        for j in range(len(a) - i - 1):
            if a[j+1] < a[j]:
                a[j+1], a[j] = a[j], a[j+1] 
                count += 1
    return count
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    print(f'Array is sorted in {countSwaps(a)} swaps.')
    print(f'First Element: {a[0]}')
    print(f'Last Element: {a[-1]}')
    
