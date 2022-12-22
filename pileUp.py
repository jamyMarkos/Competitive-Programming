# Enter your code here. Read input from STDIN. Print output to STDOUT

from typing import List

def pileUp(n: int, llist: List[int]) -> None:
    l, r = 0, n - 1
    temp = max(llist[r], llist[l])
    while r > l:
        if llist[r] > llist[l] and llist[r] <= temp:
            temp = llist[r]
            r -= 1
        elif llist[l] > llist[r] and llist[l] <= temp:
            temp = llist[l]
            l += 1
        elif llist[l] == llist[r] and llist[l] <= temp:
            temp = llist[r]
            l, r = l+1, r-1
        else:
            return 'No'
    return 'Yes'
        
  
if __name__ == "__main__":
    llist = []
    T = int(input())
    for i in range(T):
        n = int(input())
        llist = list(map(int, input().split()))
        print(pileUp(n, llist))
        
