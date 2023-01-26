# Templates for the inputs:
from typing import List
# from collections import Counter
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
    arr_len = int(input())
    arr = list(map(int, input().split()))
    
    left, right = 0, 0
    sum_ = 0
    while right < len(arr):
        max_ = arr[left]
        if arr[left] > 0:
            while right < len(arr) and arr[right] > 0:
                max_ = max(max_, arr[right])
                right += 1
            sum_ += max_
            left = right
        elif arr[left] < 0:
            max_ = arr[left]
            while right < len(arr) and arr[right] < 0 :
                max_ = max(max_, arr[right])
                right += 1
            sum_ += max_
            left = right
            
    print(sum_)
    
    
    
           
# Driver code...    
if __name__ == '__main__':
    for i in range(intInput()):
        solve()
        
        
    
    
    
        
        
