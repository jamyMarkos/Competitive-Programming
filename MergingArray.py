# Templates for the inputs:
from typing import List
# import collections
import sys

def stringInput() -> str:
    return sys.stdin.readline()
    
def listInput() -> List[int]:
    return list(map(int, input().split()))
    
def string_list() -> List[int]:
    return list(input())


def solve():
    # Write your code here...
    n, m = listInput()
    list_1 = listInput()
    list_2 = listInput()
    res = []
    first, second = 0, 0
    while first < n and second < m:
        if list_1[first] < list_2[second]:
            res.append(list_1[first])
            first += 1
        else:
            res.append(list_2[second])
            second += 1
            
    res.extend(list_1[first:])
    res.extend(list_2[second:])
    
    [print(el, end=" ") for el in res] 
        

            
# Driver code...    
if __name__ == '__main__':
    solve()
    
        
    
    
    
        
        
