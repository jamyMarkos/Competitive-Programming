from typing import List

from collections import *
from typing import List


class Solution:
    def minimumTime(self, n : int,m : int, edges : List[List[int]]) -> int:
        indeg=[0]*n
        graph=defaultdict(list)
        res=[0]*n

        for a,b in edges:
            graph[a].append(b)
            indeg[b-1]+=1

        
        queue=deque()
        
        for i in range(n):
            if indeg[i]==0:
                queue.append((i+1,1))
        
        while queue:
            
            node=queue.popleft()
            res[node[0]-1]=node[1]
            
            for neigh in graph[node[0]]:
                indeg[neigh-1]-=1
                if indeg[neigh-1]==0:
                    queue.append((neigh,node[1]+1))
                    
        return ' '.join(map(str,res))



#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()



class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a=IntArray().Input(2)
        
        
        edges=IntMatrix().Input(a[1], a[1])
        
        obj = Solution()
        res = obj.minimumTime(a[0],a[1], edges)
        
        print(res)
        

# } Driver Code Ends