class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = 0
        visit = set()
        r = c = len(isConnected)
        
        graph = defaultdict(list)
        
        for i in range(r):
            for j in range(c):
                if i != j and isConnected[i][j]:
                    graph[i+1].append(j+1)
          
        def dfs(city):
            visit.add(city)
            for nxt in graph[city]:
                if nxt not in visit:
                    dfs(nxt)
        
        for i in range(1, r+1):
            if i not in visit:
                provinces += 1
                dfs(i)
        
        return provinces
    
        
            
        