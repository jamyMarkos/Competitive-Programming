class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        visit = set()
        
        ans = set()
        
        for a, b in edges:
            graph[a].add(b)
            
        def dfs(cur):
            visit.add(cur)
            
            for nxt in graph[cur]:
                if nxt in ans:
                    ans.remove(nxt)
                if nxt not in visit:
                    dfs(nxt)
            return 
        
        print(graph)
                
        for i in range(n):
            if i not in visit:
                ans.add(i)
                dfs(i)
            
        return ans
        
        