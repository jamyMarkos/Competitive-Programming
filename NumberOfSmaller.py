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
    ptr = 0
    for el in list_2:
        while ptr < len(list_1) and el > list_1[ptr]:
            ptr += 1
        print(ptr, end=" ")
        
    
        

            
# Driver code...    
if __name__ == '__main__':
    solve()
    
        
    
    
    
        
        
