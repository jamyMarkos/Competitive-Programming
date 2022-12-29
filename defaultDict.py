# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
if __name__ == '__main__':
    defdict = defaultdict(list)
    n, m =  map(int, input().split())
    groupA, groupB = [], []
    for i in range(n):
        temp = input()
        defdict[temp].append(i+1)
    
    for j in range(m):
        groupB.append(input())
    
    for let in groupB:
        if let in defdict:
            print(" ".join(map(str, defdict[let])))
        else:
            print(-1)
                    
    
    
