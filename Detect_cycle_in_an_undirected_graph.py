from typing import List
from collections import *
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
	    visit = [-1] * V
	    q = deque()
	    def bfs():
    	    while q:
    	        cur = q.popleft()
    	        visit[cur] = 1
    	        for nbr in adj[cur]:
    	            if visit[nbr] == -1:
    	                q.append(nbr)
    	                visit[nbr] = 0
    	            elif visit[nbr] == 0:
    	                return True
    	                
    	    return False
    	     
    	        
    	for i in range(V):
    	    if visit[i] == -1:
    	        q.append(i)
    	        visit[i] = 0
    	        if bfs():
    	            return True
    	
    	return False
	        
	    
	    
	    
		


#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends