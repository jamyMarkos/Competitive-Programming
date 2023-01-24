# Templates for the inputs:
from typing import List
from collections import Counter
import sys

def intInput():
    return int(input())

def stringInput() -> str:
    return sys.stdin.readline()
    
def listInput() -> List[int]:
    return list(map(int, input().split()))
    
def string_list() -> List[int]:
    return list(input())


def solve():
    # Write your code here...
    arr_len = intInput()
    res = sorted(listInput())
    i = 0
    while i < len(res) - 1:
        if abs(res[i+1] - res[i]) > 1:
            return 'No'
        i += 1
    return 'Yes'

    
           
# Driver code...    
if __name__ == '__main__':
    for testcase in range(intInput()):
        print(solve())
    
        
    
    
    
        
        
