#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    '''
    2 4 6 8 8 
    2 4 6 6 8 
    2 4 4 6 8 
    2 3 4 6 8 
    '''
    new_arr = arr.copy()
    for i in range(n-1, -1, -1):
        if sorted(new_arr) == arr:
            break
        temp = arr[i]
        for j in range(i-1, -1, -1):
            if arr[j] > temp:
                arr[j+1] = arr[j]
                print(*arr)
            elif temp > arr[j]:
                arr[j+1] = temp
                print(*arr)
                break
            if j == 0 and arr[j] > temp:
                arr[j] = temp
                print(*arr)
                
        
            
        
            
        
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
