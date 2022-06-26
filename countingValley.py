#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    temp = [] 
    count = 0
    for i in path:
        if len(temp) == 0:
            temp.append(i)
        elif i == temp[-1]:
            temp.append(i)
        else:
            test = temp.pop()
            if len(temp) == 0 and test == 'D':
                count += 1
    return count
                
            
        
        
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
