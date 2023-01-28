# Templates for the inputs:
from typing import List
from collections import Counter
import sys

def stringInput() -> str:
    return sys.stdin.readline()
    
def listInput() -> List[int]:
    return list(map(int, input().split()))
    
def string_list() -> List[int]:
    return list(input())
def intInput() -> int:
    return int(input())

def solve():
    # Write your code here...
    res = []
    dict_1 = dict()
    dict_2 = dict()
    n, m = listInput()
    for row in range(n):
        res.append(listInput())
        
    for row in range(len(res)):
        for col in range(len(res[0])):
            if (row + col) in dict_1:
                dict_1[(row + col)] += res[row][col]
            else:
                dict_1[(row + col)] = res[row][col]
                
            if (row - col) in dict_2:
                dict_2[(row - col)] += res[row][col]
            else:
                dict_2[(row - col)] = res[row][col]

    max_ = 0
    for row in range(len(res)):
        for col in range(len(res[0])):
            temp = dict_1[(row + col)] + dict_2[(row - col)] - res[row][col]
            max_ = max(temp, max_)

    print(max_)
                
    
          
 
            
# Driver code...    
if __name__ == '__main__':
    for tt in range(intInput()):
        solve()
    
    
        
    
    
    
        
        
