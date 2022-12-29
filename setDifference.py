# Enter your code here. Read input from STDIN. Print output to STDOUT
from typing import collections

if __name__ == '__main__':
    English = int(input())
    list_e = set(list(map(int, input().split())))
    French = int(input())
    list_f = set(list(map(int, input().split())))
    
    temp = list_e.difference(list_f)
    print(len(temp))
    
    

   
